from sentence_transformers import SentenceTransformer

class TextEmbedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        AI Framework Embedder Blueprint.
        Loads the transformation model to map text into vector space.
        """
        print(f"⏳ Loading Embedding Model [{model_name}]...")
        self.model = SentenceTransformer(model_name)
        print(f"[SUCCESS] Model loaded and ready.")

    def generate_embeddings(self, processed_chunks: list) -> list:
        """
        Takes the chunk payload list from Phase 2, extracts text strings,
        generates vectors, and updates the payload nodes with their respective embeddings.
        """
        if not processed_chunks:
            print("[WARNING] No chunks provided for embedding.")
            return []

        # Extracting only text strings for bulk embedding generation (Fastest way)
        texts_to_embed = [chunk["text"] for chunk in processed_chunks]
        
        print(f"🧬 Transforming {len(texts_to_embed)} chunks into dense vectors...")
        vectors = self.model.encode(texts_to_embed, show_progress_bar=True, batch_size=32)
        
        # Mapping the generated vector back to its respective payload node
        for idx, vector in enumerate(vectors):
            processed_chunks[idx]["embedding"] = vector.tolist() # Converting numpy array to standard list for DB compatibility
            
        print(f"[SUCCESS] Vectorization complete. Dimensionality: {len(vectors[0])}")
        return processed_chunks