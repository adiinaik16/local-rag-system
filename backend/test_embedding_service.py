from app.services.embedding_service import EmbeddingService


def main():
    service = EmbeddingService()

    texts = [
        "Refund requests must be submitted within 30 days.",
        "Employees receive annual leave benefits."
    ]

    embeddings = service.embed_documents(texts)

    print(f"Embedding count: {len(embeddings)}")
    print(f"Embedding dimension: {len(embeddings[0])}")

    query_embedding = service.embed_query(
        "What is the refund policy?"
    )

    print(
        f"Query dimension: {len(query_embedding)}"
    )


if __name__ == "__main__":
    main()