from app.services.ingestion_service import (
    IngestionService
)

from app.services.embedding_service import (
    EmbeddingService
)

from app.services.vector_store_service import (
    VectorStoreService
)


def main():

    pdf_path = "storage/uploads/sample.pdf"

    

    vector_store = (
        VectorStoreService()
    )
    vector_store.reset_collection()

    ingestion_service = (
        IngestionService()
    )

    embedding_service = (
        EmbeddingService()
    )

    # Development reset

    summary = (
        ingestion_service.ingest_pdf(
            pdf_path
        )
    )

    print("\nINGESTION SUMMARY")
    print("=" * 50)

    for key, value in summary.items():
        print(f"{key}: {value}")

    print(
        "\nTotal vectors:",
        vector_store.count_documents()
    )

    query = (
        "What technologies should students use?"
    )

    query_embedding = (
        embedding_service.embed_query(
            query
        )
    )

    results = (
        vector_store.similarity_search(
            query_embedding,
            top_k=3
        )
    )

    print("\nTOP RESULTS")
    print("=" * 50)

    for result in results:

        print(
            f"\nPage: "
            f"{result['metadata']['page']}"
        )

        print(
            f"Source: "
            f"{result['metadata']['source']}"
        )

        print(
            f"Distance: "
            f"{result['distance']}"
        )

        print(
            f"\nText:\n"
            f"{result['text'][:300]}"
        )

        print("-" * 50)


if __name__ == "__main__":
    main()