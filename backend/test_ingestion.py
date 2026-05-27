from app.services.pdf_service import PDFParserService
from app.services.chunk_service import ChunkService


def main():
    sample_pdf = "storage/uploads/sample.pdf"

    parser = PDFParserService()
    chunker = ChunkService()

    print("=" * 60)
    print("STEP 1: Parsing PDF")
    print("=" * 60)

    pages = parser.parse(sample_pdf)

    print(f"Pages extracted: {len(pages)}")

    for page in pages[:2]:
        print(f"\nPage: {page['page']}")
        print(f"Source: {page['source']}")
        print(f"Preview: {page['text'][:200]}")

    print("\n" + "=" * 60)
    print("STEP 2: Chunking")
    print("=" * 60)

    chunks = chunker.chunk_pages(pages)

    print(f"Total chunks created: {len(chunks)}")

    for chunk in chunks[:5]:
        print("\n------------------------------")
        print(f"Chunk ID: {chunk['chunk_id']}")
        print(f"Page: {chunk['page']}")
        print(f"Source: {chunk['source']}")
        print(f"Text Preview:\n{chunk['text'][:300]}")


if __name__ == "__main__":
    main()