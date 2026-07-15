from app.services.gemini_service import GeminiService
from app.services.hallucination.claim_extractor import ClaimExtractor


def print_claims(title, claims):

    print("=" * 60)

    print(title)

    print("=" * 60)

    for claim in claims:

        print(
            f"[{claim.claim_index}] {claim.text}"
        )


def main():

    extractor = ClaimExtractor()

    gemini = GeminiService()

    question = "What is the maternity leave policy?"

    rag_answer = """
Employees receive 26 weeks paid maternity leave.

The policy applies to full-time staff.

The leave can be extended by 13 weeks.

I think this policy is excellent.
"""

    gemini_answer = gemini.get_gemini_answer(
        question
    )

    rag_claims = extractor.extract_claims(
        rag_answer
    )

    gemini_claims = extractor.extract_claims(
        gemini_answer
    )

    print_claims(
        "RAG CLAIMS",
        rag_claims
    )

    print()

    print_claims(
        "GEMINI CLAIMS",
        gemini_claims
    )


if __name__ == "__main__":
    main()