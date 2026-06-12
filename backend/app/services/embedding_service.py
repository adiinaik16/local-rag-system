from typing import List

from sentence_transformers import SentenceTransformer

from app.core.config import settings
from app.core.exceptions import EmbeddingError


class EmbeddingService:
    """
    Generates semantic embeddings using
    a BERT-based sentence-transformer model.
    """

    def __init__(self):
        try:
            self.model = SentenceTransformer(
                settings.EMBEDDING_MODEL
            )
        except Exception as e:
            raise EmbeddingError(
                f"Failed to load embedding model: {e}"
            )

    def embed_documents(
        self,
        texts: List[str]
    ) -> List[List[float]]:
        """
        Generate embeddings for document chunks.
        """

        try:
            embeddings = self.model.encode(
                texts,
                convert_to_numpy=True
            )

            return embeddings.tolist()

        except Exception as e:
            raise EmbeddingError(
                f"Document embedding failed: {e}"
            )

    def embed_query(
        self,
        query: str
    ) -> List[float]:
        """
        Generate embedding for user query.
        """

        try:
            embedding = self.model.encode(
                query,
                convert_to_numpy=True
            )

            return embedding.tolist()

        except Exception as e:
            raise EmbeddingError(
                f"Query embedding failed: {e}"
            )

    def get_embedding_dimension(self) -> int:
        """
        Returns vector dimension size.
        """

        try:
            sample = self.model.encode(
                "dimension_check"
            )

            return len(sample)

        except Exception as e:
            raise EmbeddingError(
                f"Failed to determine dimension: {e}"
            )