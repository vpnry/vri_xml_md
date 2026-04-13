# VRI XML to Markdown Converter

Convert Vipassana Research Institute (VRI) Tipitaka XML files to Markdown format.

## Overview

This script converts TEI.2 XML files (styled following VRI `tipitaka-latn.xsl`) into clean Markdown documents.

## Download Input Files

Download the Roman script Tipitaka XML files from the VRI repository:

```bash
# Create directory for source files
mkdir -p romn

# Download from VRI GitHub repository
# https://github.com/VipassanaTech/tipitaka-xml/tree/main/romn
```

## Usage

### Convert a Single File

```bash
python3 vri_xml_to_md.py input.xml [output.md]
```

If `output.md` is omitted, the result is written to `<input_stem>.md` in the same directory.

### Convert All Files in a Directory

```bash
python3 vri_xml_to_md.py -d romn/ -o md/

```


## Dev note

+ XML to Markdown Mapping based on `tipitaka-latn.xsl`

| XML Element | Markdown Output |
|-------------|-----------------|
| `<p rend="nikaya">` | `# Heading` (Nikāya) |
| `<p rend="book">` | `## Heading` (Book) |
| `<p rend="chapter">` | `### Heading` (Chapter) |
| `<p rend="subhead">` | `#### Sub-heading` |
| `<p rend="subsubhead">` | `##### Sub-sub-heading` |
| `<p rend="title">` | `**Title**` (bold) |
| `<p rend="centre">` | `*centred text*` (italic) |
| `<p rend="gatha1">` | `> Verse line` (indent) |
| `<p rend="gatha2">` | `> Verse line` (indent) |
| `<p rend="gatha3">` | `> Verse line` (indent) |
| `<p rend="gathalast">` | `> Verse line` (indent) |
| `<p rend="bodytext" n="N">` | Paragraph with optional number |
| `<p rend="hangnum">` | Hanging-number paragraph |
| `<p rend="unindented">` | Unindented paragraph |
| `<p rend="indent">` | Indented paragraph |
| `<hi rend="bold">` | `**bold**` |
| `<hi rend="paranum">` | `¶N` paragraph number |
| `<hi rend="dot">` | `.` (literal) |
| `<pb ed="..." n="...">` | *stripped* (page breaks removed) |
| `<note>` | `[footnote text]` |

## CLI Options

```
usage: vri_xml_to_md.py [-h] [--add-id] [-d INPUT_DIR] [-o OUTPUT_DIR] [input] [output]

Convert VRI Tipitaka XML to Markdown

positional arguments:
  input                 Path to the input .xml file
  output                Path to the output .md file (default: same dir as input, .md extension)

options:
  -h, --help            show this help message and exit
  --add-id              Prepend a sequential ID (e.g. 'P 1 = ') to each paragraph output
  -d INPUT_DIR, --input-dir INPUT_DIR
                        Convert all .xml files in the specified directory
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Directory to save the output .md files (creates if doesn't exist)
```


## License

