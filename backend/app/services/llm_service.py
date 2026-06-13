from langchain_ollama import ChatOllama

from app.core.config import settings
from app.core.exceptions import RetrievalError


class LLMService:

    def __init__(self):

        self.llm = ChatOllama(
            model=settings.OLLAMA_MODEL,
            temperature=settings.TEMPERATURE
        )

    def generate(
        self,
        prompt: str
    ) -> str:

        try:

            response = self.llm.invoke(
                prompt
            )

            return response.content

        except Exception as e:

            raise RetrievalError(
                f"LLM generation failed: {e}"
            )