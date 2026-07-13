"""
=============================================================================
NEORAG SPACE - LOCAL EMBEDDING ENGINE (OFFLINE CORE)
=============================================================================
Uses local SentenceTransformers to generate dense vector embeddings.
Zero internet connection required. Air-gapped execution guaranteed.
=============================================================================
"""

import os
from sentence_transformers import SentenceTransformer

class TextEmbedder:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Production-Grade Local AI Embedder.
        Loads the model directly from local system cache into hardware memory.
        """
        self.model_name = model_name
        print(f"⏳ Initializing Local Embedding Pipeline [{model_name}] into hardware memory...")
        
        try:
            # Load model locally (will use cached weights automatically)
            self.model = SentenceTransformer(model_name)
            print("[SUCCESS] Local Embedding Engine successfully loaded into RAM.")
        except Exception as e:
            print(f"[CRITICAL ERROR] Failed to load local SentenceTransformer model: {str(e)}")
            raise e

    def encode(self, text: str) -> list:
        """
        Generates a 384-dimensional vector for a single query string locally.
        Used dynamically during live user inference in app.py.
        """
        try:
            if not text or not isinstance(text, str):
                return []
            
            # Generate embedding locally on CPU/GPU
            vector = self.model.encode(text, show_progress_bar=False)
            return vector.tolist()
        except Exception as e:
            print(f"[EMBEDDING ERROR] Failed to generate local vector: {str(e)}")
            return []

    def generate_embeddings(self, processed_chunks: list) -> list:
        """
        Takes the chunk payload list, extracts text strings,
        generates vectors locally in bulk, and updates the payload nodes.
        """
        if not processed_chunks:
            print("[WARNING] No chunks provided for embedding.")
            return []

        # Extract text strings for bulk local vectorization
        texts_to_embed = [chunk["text"] for chunk in processed_chunks]
        
        print(f"🧬 Sending {len(texts_to_embed)} chunks to Local CPU/GPU for vectorization...")
        try:
            # Batch encoding is highly optimized in SentenceTransformers
            vectors = self.model.encode(texts_to_embed, show_progress_bar=True, batch_size=32)
            
            if len(vectors) != len(texts_to_embed):
                print("[ERROR] Local Vector generation failed: payload length mismatch.")
                return processed_chunks

            # Map the generated vector array back to its respective payload node
            for idx, vector in enumerate(vectors):
                processed_chunks[idx]["embedding"] = vector.tolist()
                
            print(f"[SUCCESS] Local Vectorization complete. Dimensionality: {len(vectors[0])} channels")
            return processed_chunks
            
        except Exception as e:
            print(f"[CRITICAL ERROR] Bulk vectorization failed: {str(e)}")
            return processed_chunks