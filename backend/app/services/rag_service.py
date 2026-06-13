from app.core.config import settings

from app.services.embedding_service import (
    EmbeddingService
)

from app.services.vector_store_service import (
    VectorStoreService
)

from app.services.llm_service import (
    LLMService
)


class RAGService:

    def __init__(self):

        self.embedding_service = (
            EmbeddingService()
        )

        self.vector_store = (
            VectorStoreService()
        )

        self.llm_service = (
            LLMService()
        )

    def build_prompt(
        self,
        question: str,
        retrieved_chunks: list
    ) -> str:

        context_parts = []

        for idx, chunk in enumerate(
            retrieved_chunks,
            start=1
        ):

            context_parts.append(
                f"""
[Source {idx}]
Document: {chunk['metadata']['source']}
Page: {chunk['metadata']['page']}

{chunk['text']}
"""
            )

        context = "\n".join(
            context_parts
        )

        prompt = f"""
You are a document question answering assistant.

Answer ONLY using the provided context.

Do not use outside knowledge.

If the answer is not present in the context, say:

"I don't know based on the provided documents."

Context:

{context}

Question:
{question}

Answer:
"""

        return prompt

    def ask(
        self,
        question: str
    ):

        query_embedding = (
            self.embedding_service.embed_query(
                question
            )
        )

        retrieved_chunks = (
            self.vector_store.similarity_search(
                query_embedding,
                top_k=settings.TOP_K
            )
        )

        prompt = self.build_prompt(
            question,
            retrieved_chunks
        )

        answer = (
            self.llm_service.generate(
                prompt
            )
        )

        return {
            "question": question,
            "answer": answer,
            "retrieved_chunks":
                retrieved_chunks,
            "prompt":
                prompt
        }