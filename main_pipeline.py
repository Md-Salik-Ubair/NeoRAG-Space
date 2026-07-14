import os
import sys

# Ensuring path adjustments align perfectly across local directories
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.ingestor import DataIngestor
from src.chunker import TextChunker
from src.embedder import TextEmbedder
from src.vector_store import LocalVectorStore

def run_rag_production_pipeline():
    print("=" * 60)
    print("🚀 --- ENTERPRISE LOCAL RAG COMPILATION CORE START --- 🚀")
    print("=" * 60)
    
    # Paths configurations matching your exact directory layout
    PDF_DIRECTORY = "./Knowledge_Source"
    JSON_DIRECTORY = "./smart_jsons"
    VECTOR_DB_FILE = "./vault_manager/vector_index.bin"
    
    # ------------------------------------------------------------------
    # PHASE 1: DATA INGESTION
    # ------------------------------------------------------------------
    print("\n📥 [PHASE 1] Running Ingestion Engine over storage targets...")
    ingestor = DataIngestor(pdf_dir=PDF_DIRECTORY, json_dir=JSON_DIRECTORY)
    ingestor.ingest_pdfs()
    ingestor.ingest_transcripts()
    
    raw_payload = ingestor.get_payload()
    print(f"📊 Extracted Raw Document Nodes: {len(raw_payload)}")
    
    if not raw_payload:
        print("[CRITICAL ERROR] Core payload returned empty. Refusing compilation.")
        return

    # ------------------------------------------------------------------
    # PHASE 2: SLIDING WINDOW CHARACTER CHUNKING
    # ------------------------------------------------------------------
    print("\n✂️ [PHASE 2] Slicing text blocks into high-density sliding windows...")
    chunker = TextChunker(chunk_size=500, chunk_overlap=100)
    final_chunks = chunker.split_documents(raw_payload)
    print(f"📊 Generated Contextual Segments: {len(final_chunks)}")

    if not final_chunks:
        print("[CRITICAL ERROR] Chunking core returned empty chunks array.")
        return

    # ------------------------------------------------------------------
    # PHASE 3: HIGH-DIMENSIONAL EMBEDDING TRANSFORM
    # ------------------------------------------------------------------
    print("\n🧬 [PHASE 3] Commencing floating matrix text-to-vector transformations...")
    embedder = TextEmbedder(model_name="all-MiniLM-L6-v2")
    embedded_payload = embedder.generate_embeddings(final_chunks)

    # ------------------------------------------------------------------
    # PHASE 4: DISK STORAGE SERIALIZATION
    # ------------------------------------------------------------------
    print("\n💾 [PHASE 4] Committing tensor matrices into active binary index file...")
    vector_db = LocalVectorStore(storage_file=VECTOR_DB_FILE)
    vector_db.store_embeddings(embedded_payload)

    print("\n" + "=" * 60)
    print("🔥 [PIPELINE SUCCESS] Local Index compilation completed flawlessly!")
    print(f"📌 Matrix Asset Path: {VECTOR_DB_FILE}")
    print(f"📌 Matrix Vector Nodes: {len(embedded_payload)} nodes fully serialized.")
    print("=" * 60)

if __name__ == "__main__":
    run_rag_production_pipeline()