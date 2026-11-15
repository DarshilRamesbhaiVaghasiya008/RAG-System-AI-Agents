import hashlib

from medrag.config import CHUNK_SIZE, CHUNK_OVERLAP
from medrag.pdf_reader import read_pdf
from medrag.config import DATA_DIR



def split_pdf(text, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    text = "".join(text.split())
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        if end < len(text):
            space = text.rfind(" ", start, end)
            if space > start:
                end = space
        chunks.append(text[start:end].strip())
        if end >= len(text):
            break
        start = max(end - chunk_overlap, start + 1)

    return [c for c in chunks if c]


def make_chunk_id(source, text):
    key = f"{source}|{text}"
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def chunk_pages(pages, source):
    chunks = []
    for page in pages:
        for text in split_pdf(page["text"]):
            chunks.append({
                "chunk_id": make_chunk_id(source, text),
                "source": source,
                "page": page["page_number"],
                "text": text,
            })
    return chunks


if __name__ == "__main__":
    file_name = "A78_17-en.pdf"
    pages = read_pdf(DATA_DIR / file_name)
    chunks = chunk_pages(pages, source=file_name)

    print("Pages: ", len(pages))
    print("Chunks:", len(chunks))
    for chunk in chunks[:2]:
        print("-" * 60)
        print("ID:  ", chunk["chunk_id"])
        print("Page:", chunk["page"])
        print("Size:", len(chunk["text"]), "characters")
        print(chunk["text"][:200])