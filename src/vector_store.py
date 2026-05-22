import os
import pickle
import numpy as np

class LocalVectorStore:
    def __init__(self, storage_file: str = "./vault_manager/vector_index.bin"):
        """
        Data Scientist Vector Storage and Mathematics Core Engine.
        Handles binary serialization and local high-dimensional matrix search queries.
        """
        self.storage_file = storage_file
        self.payload_data = []
        
        # Creating database root directory automatically if missing
        dir_name = os.path.dirname(self.storage_file)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)

    def store_embeddings(self, embedded_payload: list):
        """Serializes and dumps the entire high-dimensional vectorized payload safely to disk."""
        self.payload_data = embedded_payload
        try:
            with open(self.storage_file, 'wb') as f:
                pickle.dump(self.payload_data, f)
            print(f"[SUCCESS] Vector Store Indexed permanently at: {self.storage_file}")
        except Exception as e:
            print(f"[CRITICAL] Serialization failed: {str(e)}")

    def load_index(self) -> bool:
        """Loads the local binary vector index back into active runtime memory (RAM)."""
        if not os.path.exists(self.storage_file):
            print(f"[WARNING] Local index file not found: {self.storage_file}")
            return False
        try:
            with open(self.storage_file, 'rb') as f:
                self.payload_data = pickle.load(f)
            print(f"[SUCCESS] Loaded {len(self.payload_data)} vector nodes into active memory matrix.")
            return True
        except Exception as e:
            print(f"[ERROR] Could not deserialize index file: {str(e)}")
            return False

    def query_similarity(self, query_vector: list, top_k: int = 3) -> list:
        """
        Performs high-speed local Cosine Similarity matching over vectorized space.
        Formula applied: (A . B) / (||A|| * ||B||)
        """
        if not self.payload_data:
            # Safe runtime automatic trigger if memory matrix is unprimed
            if not self.load_index():
                return []

        q_v = np.array(query_vector)
        q_norm = np.linalg.norm(q_v)
        
        if q_norm == 0:
            return []

        scored_results = []

        # High-performance brute-force matrix array scan native to NumPy
        for node in self.payload_data:
            doc_vector = np.array(node["embedding"])
            doc_norm = np.linalg.norm(doc_vector)
            
            if doc_norm == 0:
                continue

            # Computing Cosine Angle Match Score
            dot_product = np.dot(q_v, doc_vector)
            similarity_score = dot_product / (q_norm * doc_norm)

            scored_results.append({
                "text": node["text"],
                "metadata": node["metadata"],
                "score": float(similarity_score)
            })

        # Sorting array from highest geometric similarity match to lowest
        scored_results.sort(key=lambda x: x["score"], reverse=True)
        return scored_results[:top_k]