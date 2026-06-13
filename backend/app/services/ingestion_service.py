from app.services.pdf_service import PDFParserService
from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService


class IngestionService:
    """
    Coordinates the full ingestion pipeline.

    PDF
    -> Parse
    -> Chunk
    -> Embed
    -> Store
    """

    def __init__(self):
        self.parser = PDFParserService()
        self.chunker = ChunkService()
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStoreService()

    def ingest_pdf(self, pdf_path: str) -> dict:
        """
        Ingest a PDF into the vector database.
        """

        # Step 1
        pages = self.parser.parse(pdf_path)

        # Step 2
        chunks = self.chunker.chunk_pages(pages)

        # Step 3
        embeddings = self.embedding_service.embed_documents(
            [chunk["text"] for chunk in chunks]
        )

        # Step 4
        self.vector_store.index_documents(
            chunks,
            embeddings
        )

        return {
            "pages_processed": len(pages),
            "chunks_created": len(chunks),
            "vectors_stored": len(embeddings)
        }