from google import genai

from app.core.config import settings
from google.genai.errors import ClientError, ServerError


class GeminiService:
    """
    Handles communication with Google's Gemini model.
    """

    def __init__(self):

        if not settings.GEMINI_API_KEY:
            raise ValueError(
                "Gemini API key not configured."
            )

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )


    def get_gemini_answer(self, question: str) -> str:

        prompt = (
            f"Answer this question accurately and concisely.\n\n"
            f"Question:\n{question}"
        )

        try:

            response = self.client.models.generate_content(
                model=settings.GEMINI_MODEL,
                contents=prompt
            )

            return response.text.strip()

        except ServerError:
            raise RuntimeError(
                "Gemini service is temporarily busy. "
                "Please try again in a few moments."
            )

        except ClientError as e:
            raise RuntimeError(
                f"Gemini client error: {e}"
            )

        except Exception as e:
            raise RuntimeError(
                f"Unexpected Gemini error: {e}"
            )