#!/usr/bin/env python3
"""
xml_to_md.py — Convert VRI Tipitaka XML files to Markdown.

The XML format is TEI.2 with elements styled via tipitaka-latn.xsl:
  - <p rend="nikaya"> → # Heading (Nikāya)
  - <p rend="book"> → ## Heading (Book)
  - <p rend="chapter"> → ### Heading (Chapter)
  - <p rend="subhead"> → #### Sub-heading
  - <p rend="subsubhead"> → ##### Sub-sub-heading
  - <p rend="title"> → **Title** (bold line)
  - <p rend="centre"> → *centred text* (italic, could be section separator)
  - <p rend="gatha1"> → Verse line (indented)
  - <p rend="gatha2"> → Verse line 2 (indented)
  - <p rend="gatha3"> → Verse line 3 (indented)
  - <p rend="gathalast"> → Last verse line (indented)
  - <p rend="bodytext" n="N"> → Paragraph (with optional number)
  - <p rend="hangnum"> → Hanging-number paragraph
  - <p rend="unindented"> → Unindented paragraph
  - <p rend="indent"> → Indented paragraph
  - <hi rend="bold"> → **bold**
  - <hi rend="paranum"> → ¶N paragraph number prefix
  - <hi rend="dot"> → . (literal dot, kept inline)
  - <pb ed="..." n="..."> → Stripped (page-break marker, not rendered)

Usage:
    python xml_to_md.py input.xml [output.md]
    python xml_to_md.py --input-dir /path/to/xml --output-dir /path/to/md

If output path is omitted, the result is written to <input_stem>.md in the same directory.
"""

import sys
import re
import argparse
from pathlib import Path
from xml.etree import ElementTree as ET


# ── XSL detection ────────────────────────────────────────────────────────────

def detect_xsl(xml_path: Path) -> str:
    """ Peek at the XML processing instructions to find the linked stylesheet.

    Looks for:
        <?xml-stylesheet type="text/xsl" href="..."?>

    Returns the href value or an empty string if not found.
    """
    try:
        with xml_path.open("r", encoding="utf-8") as fh:
            for line in fh:
                match = re.search(
                    r'<\?xml-stylesheet[^?]*href=["\']([^"\']+)["\']',
                    line
                )
                if match:
                    return match.group(1)
                # Stop scanning after the root element opens
                if re.search(r"<[A-Za-z]", line) and "xml-stylesheet" not in line:
                    break
    except OSError:
        pass
    return ""


# ── Text extraction helpers ───────────────────────────────────────────────────

def iter_text(elem: ET.Element) -> str:
    """ Recursively extract text from an element, applying inline formatting.

    Handles:
        <pb> → stripped (empty string)
        <hi rend="bold"> → **text**
        <hi rend="paranum"> → ¶N
        <hi rend="dot"> → . (literal character)
        other <hi> → plain text
        other elements → plain text of all descendants
    """
    parts: list[str] = []

    # The element's own leading text (before its first child)
    if elem.text:
        parts.append(elem.text)

    for child in elem:
        tag = child.tag
        rend = child.get("rend", "")

        if tag == "pb":
            # Page-break: skip entirely (but keep tail)
            pass
        elif tag == "hi":
            inner = iter_text(child)
            if rend == "bold":
                parts.append(f"**{inner}**")
            elif rend == "paranum":
                parts.append(f"**{inner}**")
            elif rend == "dot":
                # The dot element wraps "." literally
                parts.append(inner)
            else:
                parts.append(inner)
        elif tag == "note":
            # Footnote/note → wrap in square brackets
            parts.append(f"[{iter_text(child)}]")
        else:
            # Any other inline element: just recurse
            parts.append(iter_text(child))

        # tail text follows every child element (outside the child tag)
        if child.tail:
            parts.append(child.tail)

    return "".join(parts).strip()


# ── Paragraph renderers ───────────────────────────────────────────────────────

HEADING_MAP = {
    "nikaya": "# ",
    "book": "## ",
    "chapter": "### ",
    "subhead": "#### ",
    "subsubhead": "##### ",
}

VERSE_RENDS = {"gatha1", "gatha2", "gatha3", "gathalast"}


def render_paragraph(p: ET.Element) -> str | None:
    """ Convert a <p> element to its Markdown representation.

    Returns None if the element should be skipped.
    """
    rend = p.get("rend", "")
    text = iter_text(p)

    if not text:
        return None

    # Headings
    if rend in HEADING_MAP:
        prefix = HEADING_MAP[rend]
        return f"{prefix}{text}"

    # Title (bold standalone line)
    if rend == "title":
        return f"**{text}**"

    # Centred lines (section endings / colophons)
    if rend == "centre":
        return f"*{text}*"

    # Verse lines (rendered as blockquote-style indented lines)
    if rend in VERSE_RENDS:
        return f"> {text}"

    # Main body text paragraphs
    if rend in ("bodytext", "hangnum", "unindented", "indent", ""):
        n = p.get("n")
        if n:
            return f"{text}"  # paragraph number already embedded via ¶N
        return text

    # Fallback: treat as plain text
    return text


# ── Main conversion ───────────────────────────────────────────────────────────

def xml_to_markdown(xml_path: Path, add_ids: bool = False) -> str:
    """ Parse *xml_path* and return its Markdown representation as a string.

    If add_ids is True, prepends 'P {index} = ' to each paragraph block.
    """
    # --- Detect and report XSL ---
    xsl_href = detect_xsl(xml_path)
    if xsl_href:
        print(f"[info] Detected XSL stylesheet: {xsl_href}")
        if "latn" in xsl_href.lower():
            print("[info] Using Latin-script rendering rules (tipitaka-latn.xsl)")
        else:
            print(f"[warn] Unexpected stylesheet '{xsl_href}'; "
                  "falling back to tipitaka-latn rules")
    else:
        print("[warn] No xml-stylesheet PI found; assuming tipitaka-latn structure")

    # --- Parse XML ---
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # The body content is inside <text><body>
    body = root.find(".//body")
    if body is None:
        # Some files may use <text> directly
        body = root.find(".//text")
    if body is None:
        body = root  # last resort

    lines: list[str] = []
    prev_rend: str = ""
    para_idx: int = 1

    for p in body.iter("p"):
        rend = p.get("rend", "")
        md = render_paragraph(p)
        if md is None:
            continue

        if add_ids:
            md = f"P {para_idx} = {md}"
            para_idx += 1

        # Add a blank line before headings and after certain blocks
        needs_blank_before = (
            rend in HEADING_MAP
            or rend == "centre"
            or (rend in VERSE_RENDS and prev_rend not in VERSE_RENDS)
            or (rend not in VERSE_RENDS and prev_rend in VERSE_RENDS)
        )

        if lines and needs_blank_before:
            lines.append("")

        lines.append(md)
        prev_rend = rend

    return "\n".join(lines) + "\n"


# ── CLI entry point ───────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert VRI Tipitaka XML to Markdown"
    )
    parser.add_argument("input", nargs="?", help="Path to the input .xml file")
    parser.add_argument(
        "output", nargs="?",
        help="Path to the output .md file (default: same dir as input, .md extension)",
    )
    parser.add_argument(
        "--add-id", action="store_true",
        help="Prepend a sequential ID (e.g. 'P 1 = ') to each paragraph output",
    )
    parser.add_argument(
        "-d", "--input-dir",
        help="Convert all .xml files in the specified directory",
    )
    parser.add_argument(
        "-o", "--output-dir",
        help="Directory to save the output .md files (creates if doesn't exist)",
    )
    args = parser.parse_args()

    # Validate arguments
    if not args.input and not args.input_dir:
        parser.error("Must provide either input file or --input-dir")
    if args.input and args.input_dir:
        parser.error("Cannot use both input file and --input-dir")

    # Determine input files
    if args.input_dir:
        input_dir = Path(args.input_dir).resolve()
        if not input_dir.is_dir():
            print(f"[error] Directory not found: {input_dir}", file=sys.stderr)
            sys.exit(1)
        xml_files = sorted(input_dir.glob("*.xml"))
        if not xml_files:
            print(f"[warning] No .xml files found in {input_dir}")
            sys.exit(0)
    else:
        xml_files = [Path(args.input).resolve()]

    # Determine output directory
    if args.output_dir:
        output_dir = Path(args.output_dir).resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
    else:
        output_dir = None

    # Process each XML file
    total_files = len(xml_files)
    success_count = 0
    for idx, xml_path in enumerate(xml_files, 1):
        if not xml_path.exists():
            print(f"[error] File not found: {xml_path}", file=sys.stderr)
            continue

        if xml_path.is_dir():
            continue

        # Determine output path
        if output_dir:
            output_path = output_dir / xml_path.with_suffix(".md").name
        elif args.output:
            if total_files > 1:
                output_path = Path(args.output).resolve()
                if output_path.suffix:
                    output_path = output_path.parent / f"{xml_path.stem}{output_path.suffix}"
                else:
                    output_path = output_path / xml_path.with_suffix(".md").name
            else:
                output_path = Path(args.output).resolve()
        else:
            output_path = xml_path.with_suffix(".md")

        print(f"\n[info] [{idx}/{total_files}] Processing: {xml_path}")
        print(f"[info] Output: {output_path}")

        try:
            md_content = xml_to_markdown(xml_path, add_ids=args.add_id)
            output_path.write_text(md_content, encoding="utf-8")
            print(f"[done] Written {len(md_content):,} characters to {output_path}")
            success_count += 1
        except Exception as e:
            print(f"[error] Failed to process {xml_path}: {e}", file=sys.stderr)

    print(f"\n[info] Processed {total_files} file(s), {success_count} succeeded")


if __name__ == "__main__":
    main()
