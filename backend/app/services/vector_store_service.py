from typing import List, Dict

import chromadb
from chromadb.config import Settings as ChromaSettings

from app.core.config import settings
from app.core.exceptions import VectorStoreError


class VectorStoreService:
    """
    Handles vector persistence and retrieval
    using ChromaDB.
    """

    COLLECTION_NAME = "documents"

    def __init__(self):
        try:
            self.client = chromadb.PersistentClient(
                path=settings.CHROMA_PATH
            )

            self.collection = self.client.get_or_create_collection(
                name=self.COLLECTION_NAME
            )

        except Exception as e:
            raise VectorStoreError(
                f"Failed to initialize ChromaDB: {e}"
            )

    def index_documents(
        self,
        chunks: List[Dict],
        embeddings: List[List[float]]
    ) -> None:
        """
        Store chunks and embeddings.
        """

        try:
            ids = []
            documents = []
            metadatas = []

            for chunk in chunks:
                ids.append(chunk["chunk_id"])

                documents.append(
                    chunk["text"]
                )

                metadatas.append(
                    {
                        "page": chunk["page"],
                        "source": chunk["source"]
                    }
                )

            self.collection.add(
                ids=ids,
                documents=documents,
                embeddings=embeddings,
                metadatas=metadatas
            )

        except Exception as e:
            raise VectorStoreError(
                f"Indexing failed: {e}"
            )

    def similarity_search(
        self,
        query_embedding: List[float],
        top_k: int = 3
    ) -> List[Dict]:
        """
        Retrieve most similar chunks.
        """

        try:
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k
            )

            retrieved = []

            for i in range(
                len(results["ids"][0])
            ):
                retrieved.append(
                    {
                        "id":
                            results["ids"][0][i],

                        "text":
                            results["documents"][0][i],

                        "metadata":
                            results["metadatas"][0][i],

                        "distance":
                            results["distances"][0][i]
                    }
                )

            return retrieved

        except Exception as e:
            raise VectorStoreError(
                f"Search failed: {e}"
            )

    def count_documents(self) -> int:
        """
        Returns vector count.
        """

        try:
            return self.collection.count()

        except Exception as e:
            raise VectorStoreError(
                f"Count failed: {e}"
            )

    def reset_collection(self):
        """
        Clear collection.
        Useful during development.
        """

        try:
            self.client.delete_collection(
                self.COLLECTION_NAME
            )

            self.collection = (
                self.client.get_or_create_collection(
                    name=self.COLLECTION_NAME
                )
            )

        except Exception as e:
            raise VectorStoreError(
                f"Reset failed: {e}"
            )