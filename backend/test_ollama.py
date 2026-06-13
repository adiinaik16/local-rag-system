from app.services.llm_service import LLMService


def main():

    llm = LLMService()

    response = llm.generate(
        "What is Python?"
    )

    print(response)


if __name__ == "__main__":
    main()