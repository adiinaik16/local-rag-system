import json

from langchain_ollama import ChatOllama

from app.core.config import settings
from app.models.hallucination_schema import Claim


class ClaimExtractor:
    """
    Extracts objective factual claims
    from an answer using Ollama.
    """

    def __init__(self):

        self.llm = ChatOllama(
            model=settings.OLLAMA_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
            temperature=0
        )

    def extract_claims(
        self,
        answer: str
    ) -> list[Claim]:

        prompt = f"""
You are an information extraction system.

Extract ONLY objective, verifiable factual claims.

Ignore:
- opinions
- recommendations
- greetings
- explanations
- comparisons
- speculation
- uncertainty
- filler sentences

Return ONLY a JSON array of strings.

Example:

[
  "Claim 1",
  "Claim 2"
]

Do NOT include:

- markdown
- ```json
- explanations
- headings

Answer:

{answer}
"""

        response = self.llm.invoke(
            prompt
        )
        print("\nRAW OLLAMA OUTPUT")
        print("=" * 60)
        print(response.content)
        print("=" * 60)

        return self._parse_claims(
            response.content
        )

    def _parse_claims(
    self,
    text: str
) -> list[Claim]:

        try:

            cleaned = text.strip()

            # Remove markdown code fences
            if cleaned.startswith("```"):

                cleaned = cleaned.replace(
                    "```json",
                    ""
                )

                cleaned = cleaned.replace(
                    "```",
                    ""
                ).strip()

            claims = json.loads(cleaned)

            return [

                Claim(
                    claim_index=i + 1,
                    text=claim.strip()
                )

                for i, claim in enumerate(claims)

            ]

        except Exception:

            return [

                Claim(
                    claim_index=1,
                    text=text.strip()
                )

            ]