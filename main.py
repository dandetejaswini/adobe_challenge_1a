import os
import json
import fitz  # PyMuPDF

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = os.path.basename(pdf_path).replace(".pdf", "")
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for b in blocks:
            if "lines" not in b:
                continue

            for line in b["lines"]:
                text = " ".join(span["text"] for span in line["spans"]).strip()
                if not text or len(text.split()) > 20:
                    continue

                max_font = max(span["size"] for span in line["spans"])
                level = None

                if max_font >= 20:
                    level = "H1"
                elif max_font >= 16:
                    level = "H2"
                elif max_font >= 13:
                    level = "H3"

                if level:
                    outline.append({
                        "level": level,
                        "text": text,
                        "page": page_num + 1
                    })

    return title, outline


def process_all_pdfs(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            title, outline = extract_headings(pdf_path)
            
            output_json = {
                "title": title,
                "outline": outline
            }

            out_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))
            with open(out_path, "w") as f:
                json.dump(output_json, f, indent=2)


if __name__ == "__main__":
    process_all_pdfs("/app/input", "/app/output")
