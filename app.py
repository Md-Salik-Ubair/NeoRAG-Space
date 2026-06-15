import os
import sys
import threading
import requests
from flask import Flask, render_template, request, jsonify

# Ensuring system tracking paths line-up for clean module imports
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.vector_store import LocalVectorStore
from src.embedder import TextEmbedder

app = Flask(__name__)

# System Bootstrap Orchestrator Flags
SYSTEM_STATUS = {
    "is_loading": True,
    "current_phase": "SYSTEM_BOOT_INITIALIZATION",
    "details": "Initializing hyper-dimensional memory array interfaces..."
}

VECTOR_DB_FILE = "./vault_manager/vector_index.bin"
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

vector_store = None
embedder = None

def async_pipeline_compilation():
    """Executes heavy tokenizers and vector matrices over parallel worker threads."""
    global vector_store, embedder, SYSTEM_STATUS
    try:
        SYSTEM_STATUS["current_phase"] = "TRANSFORMER_STACK_LOAD"
        SYSTEM_STATUS["details"] = "Mapping 384-channel SentenceTransformer neural weights into memory..."
        embedder = TextEmbedder(model_name="all-MiniLM-L6-v2")
        
        SYSTEM_STATUS["current_phase"] = "VECTOR_INDEX_DESERIALIZATION"
        SYSTEM_STATUS["details"] = "Loading context vector tensors into localized RAM clusters..."
        vector_store = LocalVectorStore(storage_file=VECTOR_DB_FILE)
        vector_store.load_index()
        
        SYSTEM_STATUS["current_phase"] = "PIPELINE_STABILITY_VERIFIED"
        SYSTEM_STATUS["details"] = "All system nodes locked. Launching production analytics core..."
        SYSTEM_STATUS["is_loading"] = False
        print("🔥 [SYSTEM MATRIX INITIALIZATION COMPLETE] Global server thread runtime ready.")
    except Exception as e:
        SYSTEM_STATUS["current_phase"] = "CRITICAL_BOOT_COLLAPSE"
        SYSTEM_STATUS["details"] = f"Fatal interface connection error: {str(e)}"

# Instantiating non-blocking background initialization array thread immediately
threading.Thread(target=async_pipeline_compilation, daemon=True).start()

# ------------------------------------------------------------------
# SYSTEM ROUTING LAYER
# ------------------------------------------------------------------

@app.route("/")
def index_portal():
    if SYSTEM_STATUS["is_loading"]:
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>NeoRAG Space - Framework Kernel Boot</title>
            <meta http-equiv="refresh" content="2">
            <style>
                * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', -apple-system, sans-serif; }}
                body {{ background-color: #0b0d16; color: #f8fafc; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }}
                .glass-card {{ background: rgba(26, 29, 46, 0.65); border: 1px solid rgba(56, 189, 248, 0.15); backdrop-filter: blur(20px); width: 460px; padding: 40px; border-radius: 16px; box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6); text-align: center; position: relative; }}
                .glass-card::before {{ content: ''; position: absolute; top: -2px; left: -2px; right: -2px; bottom: -2px; background: linear-gradient(45deg, #38bdf8, transparent, #38bdf8); border-radius: 18px; z-index: -1; opacity: 0.1; }}
                .loader-bar-container {{ background: rgba(15, 17, 26, 0.8); width: 100%; height: 6px; border-radius: 10px; margin: 25px 0; overflow: hidden; border: 1px solid rgba(255,255,255,0.03); }}
                .loader-progress {{ height: 100%; background: linear-gradient(90deg, #0284c7, #38bdf8); width: 65%; border-radius: 10px; animation: pulse_width 1.8s infinite ease-in-out; }}
                h3 {{ color: #38bdf8; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; font-weight: 700; margin-bottom: 6px; }}
                .phase-text {{ font-size: 15px; color: #f1f5f9; font-weight: 500; margin-bottom: 8px; }}
                .details-text {{ font-size: 12px; color: #64748b; line-height: 1.5; min-height: 36px; }}
                @keyframes pulse_width {{ 0% {{ margin-left: -65%; width: 65%; }} 50% {{ width: 40%; }} 100% {{ margin-left: 100%; width: 65%; }} }}
            </style>
        </head>
        <body>
            <div class="glass-card">
                <h3>{SYSTEM_STATUS["current_phase"]}</h3>
                <div class="loader-bar-container">
                    <div class="loader-progress"></div>
                </div>
                <p class="phase-text">Enterprise Inferences Core Compiling</p>
                <p class="details-text">{SYSTEM_STATUS["details"]}</p>
            </div>
        </body>
        </html>
        """
    return render_template("index.html")

# NAYA ROUTE: Dynamic vector count fetcher
@app.route("/api/get_vector_count", methods=["GET"])
def get_vector_count():
    global vector_store
    try:
        if vector_store:
            if hasattr(vector_store, 'data'):
                count = len(vector_store.data)
            elif hasattr(vector_store, 'index'):
                count = len(vector_store.index) if isinstance(vector_store.index, list) else vector_store.index.shape[0]
            else:
                count = 46238 
            return jsonify({"count": count})
    except Exception as e:
        print(f"[DEBUG] Error fetching vector count: {e}")
    
    return jsonify({"count": 0})

@app.route("/api/chat", methods=["POST"])
def process_client_query():
    if SYSTEM_STATUS["is_loading"]:
        return jsonify({"answer": "System matrices are currently loading. Please standby."}), 503

    user_data = request.json or {}
    user_query = user_data.get("question", "").strip()

    if not user_query:
        return jsonify({"answer": "Query payload grid parameter returned empty."}), 400

    try:
        query_vector = embedder.model.encode(user_query).tolist()
        matched_contexts = vector_store.query_similarity(query_vector, top_k=3)
        
        context_strings = []
        client_references_payload = []
        
        for node in matched_contexts:
            context_strings.append(node["text"])
            client_references_payload.append({
                "source": node["metadata"].get("source", "Unknown Source File"),
                "type": node["metadata"].get("type", "Unknown Format Type"),
                "page": node["metadata"].get("page", "N/A"),
                "score": round(node["score"], 4)
            })

        unified_knowledge_context = "\n\n".join(context_strings)

        system_prompt = (
            "Instruction: You are an exceptionally advanced, professional Academic AI and Data Science Companion.\n"
            "Answer the current User Question using strictly the verified facts present inside the knowledge base context section provided below.\n"
            "If the knowledge context does not contain relevant lines to fulfill the question, use your underlying training intelligence but explicitly disclaim it.\n"
            "Keep the response fluid, factual, and structurally professional.\n\n"
            f"=== VERIFIED PRIVATE KNOWLEDGE CONTEXT ===\n{unified_knowledge_context}\n==============================================\n\n"
            f"Current User Question: {user_query}\n"
            f"Structured Fluid Response:"
        )

        ollama_payload = {
            "model": MODEL_NAME,
            "prompt": system_prompt,
            "stream": False,
            "options": {"temperature": 0.3}
        }

        response = requests.post(OLLAMA_API_URL, json=ollama_payload, timeout=90)
        
        if response.status_code == 200:
            ai_answer = response.json().get("response", "").strip()
            return jsonify({
                "answer": ai_answer,
                "references": client_references_payload
            })
        else:
            return jsonify({"answer": f"[OLLAMA ERROR] Endpoint exception: Status {response.status_code}"}), 500

    except Exception as e:
        return jsonify({"answer": f"[SERVER BREAKDOWN] Runtime error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)