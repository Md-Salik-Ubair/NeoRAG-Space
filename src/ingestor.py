import os
import json
from pypdf import PdfReader

class DataIngestor:
    def __init__(self, pdf_dir: str, json_dir: str):
        """
        Production Ingestor Engine.
        Supports page-by-page PDF extractions, JSON video transcripts, and plain Text files.
        """
        self.pdf_dir = pdf_dir
        self.json_dir = json_dir
        self.raw_documents = []  # Core payload container: [{'text': ..., 'metadata': ...}]

    def ingest_pdfs(self) -> int:
        """Scans the PDF directory, extracts page-by-page textual tokens and appends metadata."""
        count = 0
        if not os.path.exists(self.pdf_dir):
            print(f"[ERROR] PDF directory missing: {self.pdf_dir}")
            return count

        for file in os.listdir(self.pdf_dir):
            file_path = os.path.join(self.pdf_dir, file)
            
            # 1. Processing Standard PDF Formats
            if file.endswith('.pdf'):
                try:
                    reader = PdfReader(file_path)
                    for page_num, page in enumerate(reader.pages):
                        text = page.extract_text()
                        if text and text.strip():
                            self.raw_documents.append({
                                "text": text.strip(),
                                "metadata": {
                                    "source": file,
                                    "type": "pdf",
                                    "page": page_num + 1
                                }
                            })
                    count += 1
                except Exception as e:
                    print(f"[WARNING] Could not read PDF {file}: {str(e)}")
            
            # 2. Dynamic Upgrade: Processing Plain Text Formats (.txt) in the same source
            elif file.endswith('.txt'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        text = f.read()
                        if text.strip():
                            self.raw_documents.append({
                                "text": text.strip(),
                                "metadata": {
                                    "source": file,
                                    "type": "txt",
                                    "page": 1
                                }
                            })
                    count += 1
                except Exception as e:
                    print(f"[WARNING] Could not read Text file {file}: {str(e)}")
                    
        print(f"[SUCCESS] Ingested {count} Document files successfully.")
        return count

    def ingest_transcripts(self) -> int:
        """Scans video transcripts (JSON format), cleans the nested text and appends metadata."""
        count = 0
        if not os.path.exists(self.json_dir):
            print(f"[WARNING] Transcript directory missing or skipped: {self.json_dir}")
            return count

        for file in os.listdir(self.json_dir):
            if file.endswith('.json'):
                file_path = os.path.join(self.json_dir, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        
                        if isinstance(data, dict) and "text" in data:
                            text_content = data["text"]
                        elif isinstance(data, list):
                            text_content = " ".join([block.get("text", "") for block in data])
                        else:
                            text_content = str(data)

                        if text_content.strip():
                            self.raw_documents.append({
                                "text": text_content.strip(),
                                "metadata": {
                                    "source": file,
                                    "type": "transcript"
                                }
                            })
                    count += 1
                except Exception as e:
                    print(f"[WARNING] Could not read JSON {file}: {str(e)}")
        print(f"[SUCCESS] Ingested {count} Transcript JSONs successfully.")
        return count

    def get_payload(self) -> list:
        return self.raw_documents