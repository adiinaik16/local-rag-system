from app.core.config import settings

print("Model:", settings.GEMINI_MODEL)
print("Key prefix:", settings.GEMINI_API_KEY[:8])
print("Key length:", len(settings.GEMINI_API_KEY))