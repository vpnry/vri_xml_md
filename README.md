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

- XML to Markdown Mapping based on `tipitaka-latn.xsl`

| XML Element                 | Markdown Output                  |
| --------------------------- | -------------------------------- |
| `<p rend="nikaya">`         | `# Heading` (Nikāya)             |
| `<p rend="book">`           | `## Heading` (Book)              |
| `<p rend="chapter">`        | `### Heading` (Chapter)          |
| `<p rend="subhead">`        | `#### Sub-heading`               |
| `<p rend="subsubhead">`     | `##### Sub-sub-heading`          |
| `<p rend="title">`          | `**Title**` (bold)               |
| `<p rend="centre">`         | `*centred text*` (italic)        |
| `<p rend="gatha1">`         | `> Verse line` (indent)          |
| `<p rend="gatha2">`         | `> Verse line` (indent)          |
| `<p rend="gatha3">`         | `> Verse line` (indent)          |
| `<p rend="gathalast">`      | `> Verse line` (indent)          |
| `<p rend="bodytext" n="N">` | Paragraph with optional number   |
| `<p rend="hangnum">`        | Hanging-number paragraph         |
| `<p rend="unindented">`     | Unindented paragraph             |
| `<p rend="indent">`         | Indented paragraph               |
| `<hi rend="bold">`          | `**bold**`                       |
| `<hi rend="paranum">`       | `¶N` paragraph number            |
| `<hi rend="dot">`           | `.` (literal)                    |
| `<pb ed="..." n="...">`     | _stripped_ (page breaks removed) |
| `<note>`                    | `[footnote text]`                |

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

## tipitaka-markdown-for-ai

```text
tipitaka-markdown-for-ai
├── Abhidhammapiṭaka
│   ├── 01_Mūla
│   │   ├── abh01m.mul_Dhammasaṅgaṇī_Pāḷi.md
│   │   ├── abh02m.mul_Vibhaṅga_Pāḷi.md
│   │   ├── abh03m1.mul_Dhātukathā_Pāḷi.md
│   │   ├── abh03m10.mul_Paṭṭhāna_Pāḷi-4.md
│   │   ├── abh03m11.mul_Paṭṭhāna_Pāḷi-5.md
│   │   ├── abh03m2.mul_Puggalapaññatti_Pāḷi.md
│   │   ├── abh03m3.mul_Kathāvatthu_Pāḷi.md
│   │   ├── abh03m4.mul_Yamaka_Pāḷi-1.md
│   │   ├── abh03m5.mul_Yamaka_Pāḷi-2.md
│   │   ├── abh03m6.mul_Yamaka_Pāḷi-3.md
│   │   ├── abh03m7.mul_Paṭṭhāna_Pāḷi-1.md
│   │   ├── abh03m8.mul_Paṭṭhāna_Pāḷi-2.md
│   │   └── abh03m9.mul_Paṭṭhāna_Pāḷi-3.md
│   ├── 02_Aṭṭhakathā
│   │   ├── abh01a.att_Dhammasaṅgaṇi_Aṭṭhakathā.md
│   │   ├── abh02a.att_Sammohavinodanī_Aṭṭhakathā.md
│   │   └── abh03a.att_Pañcapakaraṇa_Aṭṭhakathā.md
│   └── 03_Ṭīkā
│       ├── abh01t.tik_Dhammasaṅgaṇī-mūlaṭīkā.md
│       ├── abh02t.tik_Vibhaṅga-mūlaṭīkā.md
│       ├── abh03t.tik_Pañcapakaraṇa-mūlaṭīkā.md
│       ├── abh04t.nrf_Dhammasaṅgaṇī-anuṭīkā.md
│       ├── abh05t.nrf_Pañcapakaraṇa-anuṭīkā.md
│       ├── abh06t.nrf_Abhidhammāvatāro-nāmarūpaparicchedo.md
│       ├── abh07t.nrf_Abhidhammatthasaṅgaho.md
│       ├── abh08t.nrf_Abhidhammāvatāra-purāṇaṭīkā.md
│       └── abh09t.nrf_Abhidhammamātikāpāḷi.md
├── Aṅguttaranikāya
│   ├── 01_Mūla
│   │   ├── s0401m.mul_Ekakanipāta_Pāḷi.md
│   │   ├── s0402m1.mul_Dukanipāta_Pāḷi.md
│   │   ├── s0402m2.mul_Tikanipāta_Pāḷi.md
│   │   ├── s0402m3.mul_Catukkanipāta_Pāḷi.md
│   │   ├── s0403m1.mul_Pañcakanipāta_Pāḷi.md
│   │   ├── s0403m2.mul_Chakkanipāta_Pāḷi.md
│   │   ├── s0403m3.mul_Sattakanipāta_Pāḷi.md
│   │   ├── s0404m1.mul_Aṭṭhakādinipāta_Pāḷi.md
│   │   ├── s0404m2.mul_Navakanipāta_Pāḷi.md
│   │   ├── s0404m3.mul_Dasakanipāta_Pāḷi.md
│   │   └── s0404m4.mul_Ekādasakanipāta_Pāḷi.md
│   ├── 02_Aṭṭhakathā
│   │   ├── s0401a.att_Ekakanipāta_Aṭṭhakathā.md
│   │   ├── s0402a.att_Duka-tika-catukkanipāta_Aṭṭhakathā.md
│   │   ├── s0403a.att_Pañcaka-chakka-sattakanipāta_Aṭṭhakathā.md
│   │   └── s0404a.att_Aṭṭhakādinipāta_Aṭṭhakathā.md
│   └── 03_Ṭīkā
│       ├── s0401t.tik_Ekakanipāta_Ṭīkā.md
│       ├── s0402t.tik_Duka-tika-catukkanipāta_Ṭīkā.md
│       ├── s0403t.tik_Pañcaka-chakka-sattakanipāta_Ṭīkā.md
│       └── s0404t.tik_Aṭṭhakādinipāta_Ṭīkā.md
├── Añña
│   ├── Buddha-vandanā gantha-saṅgaho
│   │   ├── e0601n.nrf_Namakkāraṭīkā.md
│   │   ├── e0602n.nrf_Mahāpaṇāmapāṭha.md
│   │   ├── e0603n.nrf_Lakkhaṇāto_buddhathomanāgāthā.md
│   │   ├── e0604n.nrf_Sutavandanā.md
│   │   ├── e0605n.nrf_Jinālaṅkāra.md
│   │   ├── e0606n.nrf_Kamalāñjali.md
│   │   ├── e0607n.nrf_Pajjamadhu.md
│   │   └── e0608n.nrf_Buddhaguṇagāthāvalī.md
│   ├── Byākaraṇa gantha-saṅgaho
│   │   ├── e0801n.nrf_Moggallānabyākaraṇaṃ.md
│   │   ├── e0802n.nrf_Kaccāyanabyākaraṇaṃ.md
│   │   ├── e0803n.nrf_Saddanītippakaraṇaṃ_padamālā.md
│   │   ├── e0804n.nrf_Saddanītippakaraṇaṃ_dhātumālā.md
│   │   ├── e0805n.nrf_Padarūpasiddhi.md
│   │   ├── e0806n.nrf_Mogallānapañcikā.md
│   │   ├── e0807n.nrf_Payogasiddhipāṭha.md
│   │   ├── e0808n.nrf_Vuttodayapāṭha.md
│   │   ├── e0809n.nrf_Abhidhānappadīpikāpāṭha.md
│   │   ├── e0810n.nrf_Abhidhānappadīpikāṭīkā.md
│   │   ├── e0811n.nrf_Subodhālaṅkārapāṭha.md
│   │   ├── e0812n.nrf_Subodhālaṅkāraṭīkā.md
│   │   └── e0813n.nrf_Bālāvatāra_gaṇṭhipadatthavinicchayasāra.md
│   ├── Leḍī sayāḍo gantha-saṅgaho
│   │   ├── e0201n.nrf_Niruttidīpanī.md
│   │   ├── e0301n.nrf_Paramatthadīpanī_Saṅgahamahāṭīkāpāṭha.md
│   │   ├── e0401n.nrf_Anudīpanīpāṭha.md
│   │   └── e0501n.nrf_Paṭṭhānuddesa_dīpanīpāṭha.md
│   ├── Nīti-gantha-saṅgaho
│   │   ├── e1001n.nrf_Kavidappaṇanīti.md
│   │   ├── e1002n.nrf_Nītimañjarī.md
│   │   ├── e1003n.nrf_Dhammanīti.md
│   │   ├── e1004n.nrf_Mahārahanīti.md
│   │   ├── e1005n.nrf_Lokanīti.md
│   │   ├── e1006n.nrf_Suttantanīti.md
│   │   ├── e1007n.nrf_Sūrassatinīti.md
│   │   ├── e1008n.nrf_Cāṇakyanīti.md
│   │   ├── e1009n.nrf_Naradakkhadīpanī.md
│   │   └── e1010n.nrf_Caturārakkhadīpanī.md
│   ├── Pakiṇṇaka-gantha-saṅgaho
│   │   ├── e1101n.nrf_Rasavāhinī.md
│   │   ├── e1102n.nrf_Sīmavisodhanīpāṭha.md
│   │   └── e1103n.nrf_Vessantaragīti.md
│   ├── Saṅgāyana-puccha vissajjanā
│   │   ├── e0901n.nrf_Dīghanikāya_pu-vi.md
│   │   ├── e0902n.nrf_Majjhimanikāya_pu-vi.md
│   │   ├── e0903n.nrf_Saṃyuttanikāya_pu-vi.md
│   │   ├── e0904n.nrf_Aṅguttaranikāya_pu-vi.md
│   │   ├── e0905n.nrf_Vinayapiṭaka_pu-vi.md
│   │   ├── e0906n.nrf_Abhidhammapiṭaka_pu-vi.md
│   │   └── e0907n.nrf_Aṭṭhakathā_pu-vi.md
│   ├── Sihaḷa-gantha-saṅgaho
│   │   ├── e1201n.nrf_Moggallāna_vuttivivaraṇapañcikā.md
│   │   ├── e1202n.nrf_Thūpavaṃsa.md
│   │   ├── e1203n.nrf_Dāṭhāvaṃsa.md
│   │   ├── e1204n.nrf_Dhātupāṭhavilāsiniyā.md
│   │   ├── e1205n.nrf_Dhātuvaṃsa.md
│   │   ├── e1206n.nrf_Hatthavanagallavihāravaṃsa.md
│   │   ├── e1207n.nrf_Jinacaritaya.md
│   │   ├── e1208n.nrf_Jinavaṃsadīpaṃ.md
│   │   ├── e1209n.nrf_Telakaṭāhagāthā.md
│   │   ├── e1210n.nrf_Milidaṭīkā.md
│   │   ├── e1211n.nrf_Padamañjarī.md
│   │   ├── e1212n.nrf_Padasādhanaṃ.md
│   │   ├── e1213n.nrf_Saddabindupakaraṇaṃ.md
│   │   ├── e1214n.nrf_Kaccāyanadhātumañjusā.md
│   │   └── e1215n.nrf_Sāmantakūṭavaṇṇanā.md
│   ├── Vaṃsa-gantha-saṅgaho
│   │   ├── e0701n.nrf_Cūḷaganthavaṃsa.md
│   │   ├── e0702n.nrf_Sāsanavaṃsa.md
│   │   └── e0703n.nrf_Mahāvaṃsa.md
│   └── Visuddhimagga
│       ├── e0101n.mul_Visuddhimagga-1.md
│       ├── e0102n.mul_Visuddhimagga-2.md
│       ├── e0103n.att_Visuddhimagga-mahāṭīkā-1.md
│       ├── e0104n.att_Visuddhimagga-mahāṭīkā-2.md
│       └── e0105n.nrf_Visuddhimagga_nidānakathā.md
├── Dīghanikāya
│   ├── 01_Mūla
│   │   ├── s0101m.mul_Sīlakkhandhavagga_Pāḷi.md
│   │   ├── s0102m.mul_Mahāvaggapāḷi.md
│   │   └── s0103m.mul_Pāthikavagga_Pāḷi.md
│   ├── 02_Aṭṭhakathā
│   │   ├── s0101a.att_Sīlakkhandhavagga_Aṭṭhakathā.md
│   │   ├── s0102a.att_Mahāvagga_Aṭṭhakathā_Dīgha.md
│   │   └── s0103a.att_Pāthikavagga_Aṭṭhakathā.md
│   └── 03_Ṭīkā
│       ├── s0101t.tik_Sīlakkhandhavagga_Ṭīkā.md
│       ├── s0102t.tik_Mahāvagga_Ṭīkā_Dīgha.md
│       ├── s0103t.tik_Pāthikavagga_Ṭīkā.md
│       ├── s0104t.nrf_Sīlakkhandhavagga-abhinavaṭīkā-1.md
│       └── s0105t.nrf_Sīlakkhandhavagga-abhinavaṭīkā-2.md
├── Khuddakanikāya
│   ├── 01_Mūla
│   │   ├── s0501m.mul_Khuddakapāṭhapāḷi.md
│   │   ├── s0502m.mul_Dhammapada_Pāḷi.md
│   │   ├── s0503m.mul_Udāna_Pāḷi.md
│   │   ├── s0504m.mul_Itivuttaka_Pāḷi.md
│   │   ├── s0505m.mul_Suttanipāta_Pāḷi.md
│   │   ├── s0506m.mul_Vimānavatthu_Pāḷi.md
│   │   ├── s0507m.mul_Petavatthu_Pāḷi.md
│   │   ├── s0508m.mul_Theragāthā_Pāḷi.md
│   │   ├── s0509m.mul_Therīgāthā_Pāḷi.md
│   │   ├── s0510m1.mul_Apadāna_Pāḷi-1.md
│   │   ├── s0510m2.mul_Apadāna_Pāḷi-2.md
│   │   ├── s0511m.mul_Buddhavaṃsa_Pāḷi.md
│   │   ├── s0512m.mul_Cariyāpiṭaka_Pāḷi.md
│   │   ├── s0513m.mul_Jātaka_Pāḷi-1.md
│   │   ├── s0514m.mul_Jātaka_Pāḷi-2.md
│   │   ├── s0515m.mul_Mahāniddesa_Pāḷi.md
│   │   ├── s0516m.mul_Cūḷaniddesa_Pāḷi.md
│   │   ├── s0517m.mul_Paṭisambhidāmagga_Pāḷi.md
│   │   ├── s0518m.nrf_Milindapañha_Pāḷi.md
│   │   ├── s0519m.mul_Nettippakaraṇa_Pāḷi.md
│   │   └── s0520m.nrf_Peṭakopadesa_Pāḷi.md
│   ├── 02_Aṭṭhakathā
│   │   ├── s0501a.att_Khuddakapāṭha_Aṭṭhakathā.md
│   │   ├── s0502a.att_Dhammapada_Aṭṭhakathā.md
│   │   ├── s0503a.att_Udāna_Aṭṭhakathā.md
│   │   ├── s0504a.att_Itivuttaka_Aṭṭhakathā.md
│   │   ├── s0505a.att_Suttanipāta_Aṭṭhakathā.md
│   │   ├── s0506a.att_Vimānavatthu_Aṭṭhakathā.md
│   │   ├── s0507a.att_Petavatthu_Aṭṭhakathā.md
│   │   ├── s0508a1.att_Theragāthā_Aṭṭhakathā-1.md
│   │   ├── s0508a2.att_Theragāthā_Aṭṭhakathā-2.md
│   │   ├── s0509a.att_Therīgāthā_Aṭṭhakathā.md
│   │   ├── s0510a.att_Apadāna_Aṭṭhakathā.md
│   │   ├── s0511a.att_Buddhavaṃsa_Aṭṭhakathā.md
│   │   ├── s0512a.att_Cariyāpiṭaka_Aṭṭhakathā.md
│   │   ├── s0513a1.att_Jātaka_Aṭṭhakathā-1.md
│   │   ├── s0513a2.att_Jātaka_Aṭṭhakathā-2.md
│   │   ├── s0513a3.att_Jātaka_Aṭṭhakathā-3.md
│   │   ├── s0513a4.att_Jātaka_Aṭṭhakathā-4.md
│   │   ├── s0514a1.att_Jātaka_Aṭṭhakathā-5.md
│   │   ├── s0514a2.att_Jātaka_Aṭṭhakathā-6.md
│   │   ├── s0514a3.att_Jātaka_Aṭṭhakathā-7.md
│   │   ├── s0515a.att_Mahāniddesa_Aṭṭhakathā.md
│   │   ├── s0516a.att_Cūḷaniddesa_Aṭṭhakathā.md
│   │   ├── s0517a.att_Paṭisambhidāmagga_Aṭṭhakathā.md
│   │   └── s0519a.att_Nettippakaraṇa_Aṭṭhakathā.md
│   └── 03_Ṭīkā
│       ├── s0501t.nrf_Nettivibhāvinī.md
│       └── s0519t.tik_Nettippakaraṇa_Ṭīkā.md
├── LICENSE.md
├── list.txt
├── Majjhimanikāya
│   ├── 01_Mūla
│   │   ├── s0201m.mul_Mūlapaṇṇāsapāḷi.md
│   │   ├── s0202m.mul_Majjhimapaṇṇāsa_Pāḷi.md
│   │   └── s0203m.mul_Uparipaṇṇāsa_Pāḷi.md
│   ├── 02_Aṭṭhakathā
│   │   ├── s0201a.att_Mūlapaṇṇāsa_Aṭṭhakathā.md
│   │   ├── s0202a.att_Majjhimapaṇṇāsa_Aṭṭhakathā.md
│   │   └── s0203a.att_Uparipaṇṇāsa_Aṭṭhakathā.md
│   └── 03_Ṭīkā
│       ├── s0201t.tik_Mūlapaṇṇāsa_Ṭīkā.md
│       ├── s0202t.tik_Majjhimapaṇṇāsa_Ṭīkā.md
│       └── s0203t.tik_Uparipaṇṇāsa_Ṭīkā.md
├── Saṃyuttanikāya
│   ├── 01_Mūla
│   │   ├── s0301m.mul_Sagāthāvagga_Pāḷi.md
│   │   ├── s0302m.mul_Nidānavagga_Pāḷi.md
│   │   ├── s0303m.mul_Khandhavagga_Pāḷi.md
│   │   ├── s0304m.mul_Saḷāyatanavagga_Pāḷi.md
│   │   └── s0305m.mul_Mahāvagga_Pāḷi_Saṃyutta.md
│   ├── 02_Aṭṭhakathā
│   │   ├── s0301a.att_Sagāthāvagga_Aṭṭhakathā.md
│   │   ├── s0302a.att_Nidānavagga_Aṭṭhakathā.md
│   │   ├── s0303a.att_Khandhavagga_Aṭṭhakathā.md
│   │   ├── s0304a.att_Saḷāyatanavagga_Aṭṭhakathā.md
│   │   └── s0305a.att_Mahāvagga_Aṭṭhakathā_Saṃyutta.md
│   └── 03_Ṭīkā
│       ├── s0301t.tik_Sagāthāvagga_Ṭīkā.md
│       ├── s0302t.tik_Nidānavagga_Ṭīkā.md
│       ├── s0303t.tik_Khandhavagga_Ṭīkā.md
│       ├── s0304t.tik_Saḷāyatanavagga_Ṭīkā.md
│       └── s0305t.tik_Mahāvagga_Ṭīkā_Saṃyutta.md
└── Vinayapiṭaka
    ├── 01_Mūla
    │   ├── vin01m.mul_Pārājikapāḷi.md
    │   ├── vin02m1.mul_Pācittiyapāḷi.md
    │   ├── vin02m2.mul_Mahāvagga_Pāḷi_Vinaya.md
    │   ├── vin02m3.mul_Cūḷavagga_Pāḷi.md
    │   └── vin02m4.mul_Parivāra_Pāḷi.md
    ├── 02_Aṭṭhakathā
    │   ├── vin01a.att_Pārājikakaṇḍa_Aṭṭhakathā.md
    │   ├── vin02a1.att_Pācittiya-aṭṭhakathā.md
    │   ├── vin02a2.att_Mahāvagga_Aṭṭhakathā_Vinaya.md
    │   ├── vin02a3.att_Cūḷavagga_Aṭṭhakathā.md
    │   └── vin02a4.att_Parivāra_Aṭṭhakathā.md
    └── 03_Ṭīkā
        ├── vin01t1.tik_Sāratthadīpanī_Ṭīkā-1.md
        ├── vin01t2.tik_Sāratthadīpanī_Ṭīkā-2.md
        ├── vin02t.tik_Sāratthadīpanī_Ṭīkā-3.md
        ├── vin04t.nrf_Dvemātikāpāḷi.md
        ├── vin05t.nrf_Vinayasaṅgaha_Aṭṭhakathā.md
        ├── vin06t.nrf_Vajirabuddhi_Ṭīkā.md
        ├── vin07t.nrf_Vimativinodanī_Ṭīkā.md
        ├── vin08t.nrf_Vinayālaṅkāra_Ṭīkā.md
        ├── vin09t.nrf_Kaṅkhāvitaraṇīpurāṇa_Ṭīkā.md
        ├── vin10t.nrf_Vinayavinicchaya-uttaravinicchaya.md
        ├── vin11t.nrf_Vinayavinicchaya_Ṭīkā.md
        ├── vin12t.nrf_Pācityādiyojanāpāḷi.md
        └── vin13t.nrf_Khuddasikkhā-mūlasikkhā.md

39 directories, 219 files


```
