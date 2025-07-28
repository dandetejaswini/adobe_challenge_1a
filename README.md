
# PDF Outline Extractor – Adobe Hackathon Round 1A

## Overview

This project is a solution for Round 1A of the Adobe India Hackathon 2025, under the "Connecting the Dots" challenge.

The goal is to extract a structured outline from a given PDF document, including:

- Title
- Headings (H1, H2, H3)
- Page numbers

The output is a JSON file in the following format:

```json
{
  "title": "Sample PDF",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "Overview", "page": 2 },
    { "level": "H3", "text": "Details", "page": 3 }
  ]
}
````

## Features

* Supports PDF documents up to 50 pages
* Extracts headings based on font size heuristics
* Fast processing with no external dependencies
* Runs entirely offline
* Outputs one JSON file for each PDF

## File Structure

```
project-root/
│
├── Dockerfile
├── main.py
├── requirements.txt
├── input/             # Folder to place input PDFs
├── output/            # Folder where output JSONs are saved
└── README.md
```

## Requirements

* Docker installed and running
* No internet access required during execution

## How to Build and Run

### 1. Place all input PDFs in the `input/` folder

```bash
project-root/
└── input/
    └── example.pdf
```

### 2. Build the Docker image

```bash
docker build --platform=linux/amd64 -t adobe_outline_extractor .
```

### 3. Run the container

#### If using PowerShell:

```bash
docker run --rm -v ${PWD}/input:/app/input -v ${PWD}/output:/app/output --network none adobe_outline_extractor
```

#### If using Command Prompt (CMD):

```cmd
docker run --rm -v %cd%/input:/app/input -v %cd%/output:/app/output --network none adobe_outline_extractor
```

### 4. Output

Check the `output/` directory. For each `filename.pdf`, a corresponding `filename.json` will be generated.

## Approach

We use PyMuPDF (`fitz`) to extract all text elements from the PDF page-wise, preserving font size and positioning metadata. Based on font size heuristics:

* Font size >= 20 → H1
* Font size >= 16 → H2
* Font size >= 13 → H3

Each detected heading is stored along with its page number. The final result is output in the required JSON format.

## Libraries Used

* PyMuPDF for PDF parsing and text extraction
* json, os for filesystem and output formatting

## Notes

* Model size: No ML model used; lightweight and fully offline
* Execution Time: Well within 10 seconds on 50-page documents
* Architecture: Compatible with AMD64 (x86\_64) CPUs
* No hardcoded logic, no internet usage, no API calls, no GPU

