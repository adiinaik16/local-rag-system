from app.services.rag_service import (
    RAGService
)


def main():

    rag = RAGService()

    question = (
        "What technologies should students use?"
    )

    result = rag.ask(
        question
    )

    print("\nQUESTION")
    print("=" * 60)
    print(result["question"])

    print("\nRETRIEVED CHUNKS")
    print("=" * 60)

    for idx, chunk in enumerate(
        result["retrieved_chunks"],
        start=1
    ):

        print(
            f"\n[Source {idx}]"
        )

        print(
            f"Document: "
            f"{chunk['metadata']['source']}"
        )

        print(
            f"Page: "
            f"{chunk['metadata']['page']}"
        )

        print(
            f"Distance: "
            f"{chunk['distance']}"
        )

        print(
            f"\n{chunk['text'][:300]}"
        )

        print(
            "-" * 60
        )

    print("\nPROMPT SENT TO LLM")
    print("=" * 60)

    print(
        result["prompt"]
    )

    print("\nFINAL ANSWER")
    print("=" * 60)

    print(
        result["answer"]
    )


if __name__ == "__main__":
    main()