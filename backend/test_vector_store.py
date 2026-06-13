from app.services.embedding_service import (
    EmbeddingService
)

from app.services.vector_store_service import (
    VectorStoreService
)


def main():

    embedding_service = (
        EmbeddingService()
    )

    vector_store = (
        VectorStoreService()
    )

    vector_store.reset_collection()

    chunks = [
        {
            "chunk_id": "1",
            "text":
                "Refund requests must be submitted within 30 days.",
            "page": 1,
            "source": "test.pdf"
        },
        {
            "chunk_id": "2",
            "text":
                "Employees receive annual leave benefits.",
            "page": 2,
            "source": "test.pdf"
        }
    ]

    embeddings = (
        embedding_service.embed_documents(
            [
                chunk["text"]
                for chunk in chunks
            ]
        )
    )

    vector_store.index_documents(
        chunks,
        embeddings
    )

    print(
        "Stored vectors:",
        vector_store.count_documents()
    )

    query_embedding = (
        embedding_service.embed_query(
            "What is the refund policy?"
        )
    )

    results = (
        vector_store.similarity_search(
            query_embedding,
            top_k=2
        )
    )

    print("\nResults:\n")

    for result in results:
        print(result)
        print("-" * 50)


if __name__ == "__main__":
    main()