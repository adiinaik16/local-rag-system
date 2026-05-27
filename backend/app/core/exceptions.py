class RAGException(Exception):
    """Base domain exception."""


class FileProcessingError(RAGException):
    """PDF extraction failure."""


class InvalidFileTypeError(RAGException):
    """Unsupported file type."""


class EmbeddingError(RAGException):
    """Embedding generation failure."""


class VectorStoreError(RAGException):
    """Vector DB operation failure."""


class RetrievalError(RAGException):
    """Retrieval failure."""


class LLMGenerationError(RAGException):
    """LLM generation failure."""


class ConfigurationError(RAGException):
    """Configuration issue."""