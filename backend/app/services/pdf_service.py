from pathlib import Path
from typing import List, Dict

import fitz  # PyMuPDF

from app.core.exceptions import FileProcessingError


class PDFParserService:
    """
    Responsible for extracting text from PDF files
    while preserving page metadata.
    """

    def parse(self, pdf_path: str) -> List[Dict]:
        """
        Extract text page by page.

        Returns:
            [
                {
                    "page": 1,
                    "text": "...",
                    "source": "sample.pdf"
                }
            ]
        """

        path = Path(pdf_path)

        if not path.exists():
            raise FileProcessingError(f"File not found: {pdf_path}")

        try:
            document = fitz.open(pdf_path)
        except Exception as e:
            raise FileProcessingError(f"Failed to open PDF: {e}")

        extracted_pages = []

        try:
            for page_index in range(len(document)):
                page = document[page_index]
                text = page.get_text("text").strip()

                if not text:
                    continue

                extracted_pages.append(
                    {
                        "page": page_index + 1,
                        "text": text,
                        "source": path.name
                    }
                )

            document.close()
            return extracted_pages

        except Exception as e:
            raise FileProcessingError(f"PDF parsing failed: {e}")