import os
import sys
import requests
import json

# Ensuring system tracking paths are structurally matching local setups
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.embedder import TextEmbedder
from src.vector_store import LocalVectorStore

class LocalRAGQueryEngine:
    def __init__(self, ollama_model: str = "llama3"):
        """
        100% Offline Local Inference Engine via Ollama API framework.
        Fuses high-dimensional matrix search directly with local open-source LLMs.
        """
        print("🤖 Initializing Local RAG Context Query Engine Components...")
        
        # 1. Bootstrapping local components
        self.embedder = TextEmbedder()
        self.vector_db = LocalVectorStore(storage_file="./vault_manager/vector_index.bin")
        
        # Safe loading vector database matrix into RAM
        if not self.vector_db.load_index():
            print("[CRITICAL] Index loading collapsed. Please check your vault_manager files.")
            sys.exit(1)
            
        # 2. Ollama Configuration Settings
        self.ollama_url = "http://localhost:11434/api/generate"
        self.target_model = ollama_model
        print(f"[SUCCESS] Local Ollama Pipeline Target Set to Model: {self.target_model}\n")

    def execute_inference(self, user_question: str) -> str:
        """
        Processes query locally, applies Cosine thresholds, wraps contextual tokens,
        and fires native local API request to Ollama endpoint.
        """
        # Step A: Transforming user input into embedding query channel using local model
        query_text_list = [{"text": user_question}]
        vectorized_payload = self.embedder.generate_embeddings(query_text_list)
        query_vector = vectorized_payload[0]["embedding"]
        
        # Step B: Gathering top 3 closest contextual knowledge chunks via Cosine matching
        print("🔍 Searching local database matrix for relevant citations...")
        matched_context_nodes = self.vector_db.query_similarity(query_vector, top_k=3)
        
        if not matched_context_nodes:
            return "Unable to retrieve valid context frames from storage drive."

        # Building context block with source details
        context_accumulator = []
        print("\n📚 --- RETRIEVED REFERENCES FOR QUERY ---")
        for idx, node in enumerate(matched_context_nodes):
            meta = node["metadata"]
            print(f"   [{idx+1}] File: {meta.get('source')} | Type: {meta.get('type')} | Score: {node['score']:.4f}")
            context_accumulator.append(node["text"])
        print("-" * 40)

        unified_context_text = "\n\n".join(context_accumulator)

        # Step C: Engineering Core System Prompts
        full_system_prompt = (
            f"Instruction: You are a God-Level Academic AI and Data Science Assistant Expert.\n"
            f"Answer the user's technical question based strictly on the provided context chunks below.\n"
            f"If the context does not contain relevant information, use your technical knowledge but explicitly mention it.\n"
            f"Keep the language highly professional, accurate, clear, and perfectly formatted.\n\n"
            f"=== ACADEMIC KNOWLEDGE BASE CONTEXT ===\n{unified_context_text}\n=========================================\n\n"
            f"User Question: {user_question}\n"
            f"Final Accurate Answer:"
        )

        # Step D: Firing Local Ollama API Request Payload
        print(f"🧠 Synthesizing final answer locally via Ollama [{self.target_model}]...")
        
        payload = {
            "model": self.target_model,
            "prompt": full_system_prompt,
            "stream": False,  # Kept false for a clean aggregated output delivery
            "options": {
                "temperature": 0.2  # Low temperature restricts hallucinations
            }
        }

        try:
            response = requests.post(self.ollama_url, json=payload, timeout=90)
            if response.status_code == 200:
                response_json = response.json()
                return response_json.get("response", "No text generated.")
            else:
                return f"[OLLAMA ERROR] Endpoint returned status code: {response.status_code} - {response.text}"
        except requests.exceptions.ConnectionError:
            return "[CRITICAL CONNECTION ERROR] Ollama is not running! Please run 'ollama serve' or open the Ollama app."
        except Exception as e:
            return f"[LOCAL EXCEPTION] Failed to execute local pipeline: {str(e)}"

if __name__ == "__main__":
    # Standard runtime loop activation
    # Change "llama3" to "llama3.1", "mistral", or whatever model name you have active in Ollama
    ACTIVE_MODEL = "llama3" 
    
    engine = LocalRAGQueryEngine(ollama_model=ACTIVE_MODEL)
    
    print(f"✨ --- LIVE OFFLINE LOCAL OLLAMA INFERENCE USER TERMINAL ACTIVE --- ✨")
    print("Type 'exit' or 'quit' anytime to shut down active environment execution loop.\n")
    
    while True:
        user_input = input("❓ Enter your technical query: ")
        if user_input.strip().lower() in ['exit', 'quit']:
            print("\nShutting down local engine environment pipelines. System terminated safely.")
            break
            
        if not user_input.strip():
            continue
            
        answer = engine.execute_inference(user_input)
        print("\n👑 --- LOCAL MASTER MODEL AI GENERATION --- 👑")
        print(answer)
        print("=" * 70 + "\n")