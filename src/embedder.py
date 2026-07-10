import os
import time
import requests

class TextEmbedder:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Production-Grade Cloud AI Framework Embedder Blueprint.
        Uses Hugging Face Inference API to generate vectors, saving local RAM.
        """
        self.model_name = model_name
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        
        # Retrieve Hugging Face API key from environment variables
        self.hf_token = os.getenv("HF_API_KEY")
        if not self.hf_token:
            print("[CRITICAL ERROR] HF_API_KEY not found in environment variables. Vectorization will fail.")
            
        self.headers = {"Authorization": f"Bearer {self.hf_token}"}
        print(f"⏳ Initializing Cloud Embedding Pipeline via Hugging Face API [{model_name}]...")

    def _query_huggingface(self, payload, max_retries=3):
        """Internal method to handle API requests with robust retry logic."""
        for attempt in range(max_retries):
            try:
                response = requests.post(self.api_url, headers=self.headers, json=payload)
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 503:
                    # Model is currently loading/waking up on HF servers
                    estimated_time = response.json().get("estimated_time", 15)
                    print(f"[WAIT] Cloud model is booting up. Retrying in {estimated_time} seconds...")
                    time.sleep(estimated_time)
                else:
                    print(f"[ERROR] API Request failed with status {response.status_code}: {response.text}")
                    return []
            except Exception as e:
                print(f"[EXCEPTION] API connection error: {str(e)}")
                return []
        return []

    def encode(self, text: str) -> list:
        """
        Generates a vector for a single query string.
        Used dynamically during live user inference in app.py.
        """
        vectors = self._query_huggingface({"inputs": text})
        if vectors and isinstance(vectors, list):
            # API returns a list of floats for a single string
            return vectors
        return []

    def generate_embeddings(self, processed_chunks: list) -> list:
        """
        Takes the chunk payload list, extracts text strings,
        generates vectors via Cloud API in bulk, and updates the payload nodes.
        """
        if not processed_chunks:
            print("[WARNING] No chunks provided for embedding.")
            return []

        # Extracting text strings for bulk cloud vectorization
        texts_to_embed = [chunk["text"] for chunk in processed_chunks]
        
        print(f"🧬 Sending {len(texts_to_embed)} chunks to Cloud API for vectorization...")
        vectors = self._query_huggingface({"inputs": texts_to_embed})
        
        if not vectors or len(vectors) != len(texts_to_embed):
            print("[ERROR] Cloud Vector generation failed or payload length mismatch.")
            return processed_chunks

        # Mapping the generated vector array back to its respective payload node
        for idx, vector in enumerate(vectors):
            processed_chunks[idx]["embedding"] = vector 
            
        print(f"[SUCCESS] Cloud Vectorization complete. Dimensionality: {len(vectors[0])} channels")
        return processed_chunks