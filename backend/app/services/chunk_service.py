from typing import List, Dict

from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkService:
    """
    Responsible for splitting extracted PDF text
    into retrieval-friendly chunks.
    """

    def __init__(
        self,
        chunk_size: int = 512,
        chunk_overlap: int = 100
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ". ", " ", ""]
        )

    def chunk_pages(self, pages: List[Dict]) -> List[Dict]:
        """
        Converts parsed pages into chunked documents
        while preserving metadata.
        """

        chunks = []

        for page_data in pages:
            split_chunks = self.splitter.split_text(page_data["text"])

            for index, chunk in enumerate(split_chunks):
                chunks.append(
                    {
                        "chunk_id": f"{page_data['source']}_p{page_data['page']}_c{index}",
                        "text": chunk,
                        "page": page_data["page"],
                        "source": page_data["source"]
                    }
                )

        return chunks