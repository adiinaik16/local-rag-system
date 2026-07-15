from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Local RAG System"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    API_PREFIX: str = "/api/v1"

    EMBEDDING_MODEL: str = "sentence-transformers/bert-base-nli-mean-tokens"
    OLLAMA_MODEL: str = "llama3.2:latest"
    # LLM_MODEL: str = "llama3.2"

    GEMINI_API_KEY: str = ""

    GEMINI_MODEL: str = (
        "gemini-3.5-flash"
    )

    HALLUCINATION_DETECTION_ENABLED: bool = True

    HALLUCINATION_THRESHOLD: float = 0.25

    NLI_MODEL: str = (
        "cross-encoder/nli-deberta-v3-small"
    )

    CHROMA_PATH: str = "storage/chroma"
    UPLOAD_PATH: str = "storage/uploads"
    LOG_PATH: str = "storage/logs"

    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 100

    TOP_K: int = 5
    MAX_FILE_SIZE_MB: int = 20
    ALLOWED_EXTENSIONS: list[str] = ["pdf"]

    OLLAMA_BASE_URL: str = "http://localhost:11434"
    
    TEMPERATURE: float = 0.0

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()