import pymupdf

from medrag.config import DATA_DIR

def read_pdf(path):
    pages = []
    with pymupdf.open(path) as pdf:
        for page_number, page in enumerate(pdf, start=1):
            text = page.get_text()
            pages.append({"page_number": page_number, "text": text})
    return pages


if __name__ == "__main__":
    pdf_path = DATA_DIR / "A78_17-en.pdf"
    pages = read_pdf(pdf_path)
    print("Number of pages:", len(pages))
    print(pages[0]["text"][:500])