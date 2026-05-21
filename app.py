import os
import sys
import requests
from flask import Flask, render_template, request, jsonify

# Fixing workspace module lookups structure paths
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.embedder import TextEmbedder
from src.vector_store import LocalVectorStore
from src.memory_manager import ConversationMemoryManager

app = Flask(__name__)

# Initializing global operational framework layers locally
print("🚀 --- BOOTSTRAPPING PRODUCTION WEB SERVERS FRAMEWORKS --- 🚀")
embedder_engine = TextEmbedder()
vector_store_db = LocalVectorStore(storage_file="./vault_manager/vector_index.bin")
memory_engine = ConversationMemoryManager(max_turns=5)

# Forcing vector indices into active server RAM
if not vector_store_db.load_index():
    print("[CRITICAL] Vector index unavailable. Run main_pipeline.py compilation first.")
    sys.exit(1)

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_MODEL_TAG = "llama3"

@app.route('/')
def load_dashboard_view():
    """Renders the top-tier dark user interface view layer template."""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def process_client_query():
    """Handles async post payloads, scores vectors, injects memory buffers and resolves inferences."""
    payload = request.get_json() or {}
    user_question = payload.get("question", "").strip()
    
    if not user_question:
        return jsonify({"answer": "Query text parameter returned empty grid."}), 400

    try:
        # Step A: Vectorizing the incoming user query string layout
        vectorized_bundle = embedder_engine.generate_embeddings([{"text": user_question}])
        query_vector = vectorized_bundle[0]["embedding"]
        
        # Step B: Gathering top 3 matrix matches via local Cosine formulas
        closest_matches = vector_store_db.query_similarity(query_vector, top_k=3)
        
        # Building structural contexts array arrays for template view injections
        context_strings = []
        client_references_payload = []
        
        for node in closest_matches:
            context_strings.append(node["text"])
            client_references_payload.append({
                "source": node["metadata"].get("source", "Unknown Source File"),
                "type": node["metadata"].get("type", "Unknown Format Type"),
                "page": node["metadata"].get("page", None),
                "score": node["score"]
            })
            
        unified_knowledge_text = "\n\n".join(context_strings)
        
        # Step C: Appending current state into multi-turn conversational history strings
        rolling_chat_history = memory_engine.get_formatted_history()
        
        # Step D: Engineering tight contextual instructions parameters to minimize hallucinations
        hyper_prompt = (
            f"Instruction: You are an exceptionally advanced, professional Academic AI and Data Science Companion.\n"
            f"Answer the current User Question using strictly the verified facts present inside the knowledge base context section provided below.\n"
            f"If the knowledge context does not contain relevant lines to fulfill the question, use your underlying training intelligence but explicitly disclaim it.\n"
            f"Never make up false data points or cite pages that do not exist.\n\n"
            f"=== VERIFIED PRIVATED DATA KNOWLEDGE BASE ===\n{unified_knowledge_text}\n==============================================\n\n"
            f"=== ROLLING INTERACTION HISTORY RECORD ===\n{rolling_chat_history}==========================================\n\n"
            f"Current User Question: {user_question}\n"
            f"Structured Fluid Response:"
        )
        
        # Step E: Transferring payload requests to native local ports via HTTP Post requests
        ollama_request_body = {
            "model": OLLAMA_MODEL_TAG,
            "prompt": hyper_prompt,
            "stream": False,
            "options": {
                "temperature": 0.2
            }
        }
        
        response = requests.post(OLLAMA_ENDPOINT, json=ollama_request_body, timeout=120)
        
        if response.status_code == 200:
            ai_answer = response.json().get("response", "Execution stack returned a blank output trace.").strip()
            # Committing transaction state safely into conversational memory logs
            memory_engine.append_message("user", user_question)
            memory_engine.append_message("assistant", ai_answer)
            
            return jsonify({
                "answer": ai_answer,
                "references": client_references_payload
            })
        else:
            return jsonify({"answer": f"[LOCAL OLLAMA ERROR CODE {response.status_code}] Framework connection rejected."}), 500
            
    except requests.exceptions.ConnectionError:
        return jsonify({"answer": "[CRITICAL PORT ERROR] Local Ollama backend service instance is unresponsive. Ensure 'ollama serve' is active."}), 500
    except Exception as e:
        return jsonify({"answer": f"[RUNTIME CORE SYSTEM ERROR] Exception caught: {str(e)}"}), 500

@app.route('/api/clear', methods=['POST'])
def wipe_session_memory_buffer():
    """Triggers rolling dialogue history flushes safely."""
    memory_engine.clear_memory()
    return jsonify({"status": "Session track flushed."})

if __name__ == "__main__":
    # Launching local production server blocks across default web developer ports
    app.run(host="127.0.0.1", port=5000, debug=False)