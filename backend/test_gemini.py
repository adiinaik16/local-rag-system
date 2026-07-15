from app.services.gemini_service import GeminiService


def main():

    gemini = GeminiService()

    question = (
        "What is the maternity leave policy?"
    )

    answer = (
        gemini.get_gemini_answer(
            question
        )
    )

    print("=" * 60)
    print("QUESTION")
    print("=" * 60)

    print(question)

    print("\n")

    print("=" * 60)
    print("GEMINI ANSWER")
    print("=" * 60)

    print(answer)


if __name__ == "__main__":
    main()