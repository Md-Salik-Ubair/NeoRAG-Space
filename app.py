"""
=============================================================================
NEORAG SPACE - ENTERPRISE LOCAL KNOWLEDGE INTELLIGENCE ENGINE (FROZEN CORE)
=============================================================================
Architecture : Standalone Air-Gapped RAG Router
Inference    : Local Ollama (Llama 3 / Custom LLM)
Embeddings   : Local SentenceTransformers (all-MiniLM-L6-v2)
Vector Store : Dense Binary Vault (Cosine Similarity)
=============================================================================
"""

import os
import sys

# 1. FORCE HUGGINGFACE TO 100% OFFLINE MODE (CRASH FIX)
# Must be set before any local ML libraries are parsed
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import threading
import time
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Ensure local custom modules can be imported cleanly
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.vector_store import LocalVectorStore
from src.embedder import TextEmbedder

# Initialize Environment configuration
load_dotenv()

app = Flask(__name__)

# =====================================================================
# LOCAL CORE CONFIGURATION (FROZEN)
# =====================================================================
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")
MODEL_NAME = os.getenv("LOCAL_MODEL_NAME", "llama3")
VECTOR_DB_FILE = "./vault_manager/vector_index.bin"

# Global System Telemetry State
SYSTEM_STATUS = {
    "is_loading": True,
    "current_phase": "SYSTEM_BOOT_INITIALIZATION",
    "details": "Initializing Air-Gapped Local Knowledge Intelligence Platform..."
}

vector_store = None
embedder = None


# =====================================================================
# ASYNCHRONOUS VAULT & EMBEDDER COMPILATION (NON-BLOCKING BOOT)
# =====================================================================
def async_pipeline_compilation():
    global vector_store, embedder, SYSTEM_STATUS

    try:
        os.makedirs(os.path.dirname(VECTOR_DB_FILE), exist_ok=True)

        # Phase 1: Load Local Embedding Engine
        SYSTEM_STATUS["current_phase"] = "EMBEDDING_ENGINE_LOADING"
        SYSTEM_STATUS["details"] = "Loading Local SentenceTransformer (MiniLM-L6-v2) into memory..."
        print("[TELEMETRY] Initializing Local Embedding Model...")
        embedder = TextEmbedder(model_name="sentence-transformers/all-MiniLM-L6-v2")

        # Phase 2: Load Binary Knowledge Vault
        SYSTEM_STATUS["current_phase"] = "VECTOR_DATABASE_LOADING"
        SYSTEM_STATUS["details"] = "Reading high-dimensional vector index from disk..."
        print("[TELEMETRY] Loading Vector Index Vault...")
        vector_store = LocalVectorStore(storage_file=VECTOR_DB_FILE)
        vector_store.load_index()

        # Phase 3: System Ready Lock
        SYSTEM_STATUS["current_phase"] = "SYSTEM_READY"
        SYSTEM_STATUS["details"] = "Enterprise Knowledge Platform Ready. Offline Isolated Mode Active."
        SYSTEM_STATUS["is_loading"] = False
        print("[TELEMETRY] Local RAG Architecture Fully Operational.")

    except Exception as e:
        SYSTEM_STATUS["current_phase"] = "BOOT_FAILED"
        SYSTEM_STATUS["details"] = f"CRITICAL BOOT ERROR: {str(e)}"
        print(f"[CRITICAL ERROR] Pipeline Compilation Failed: {str(e)}")


# Trigger asynchronous compilation immediately on server startup
threading.Thread(target=async_pipeline_compilation, daemon=True).start()


# =====================================================================
# API GATEWAY & ROUTING MECHANICS
# =====================================================================
@app.route("/")
def home():
    """Serves the intelligent loading dashboard during boot, then switches to UI."""
    if SYSTEM_STATUS["is_loading"]:
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="refresh" content="1.5">
            <title>NeoRAG Space | Booting...</title>
            <style>
                body {{ background: #05080f; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; }}
                .box {{ width: 520px; text-align: center; padding: 40px; background: rgba(13, 20, 36, 0.85); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); backdrop-filter: blur(10px); }}
                h2 {{ color: #38bdf8; margin-bottom: 15px; font-weight: 700; font-size: 18px; letter-spacing: 1px; text-transform: uppercase; }}
                p {{ color: #94a3b8; font-size: 14px; line-height: 1.5; }}
                .loader {{ border: 3px solid rgba(255,255,255,0.05); border-top: 3px solid #38bdf8; border-radius: 50%; width: 44px; height: 44px; animation: spin 0.8s linear infinite; margin: 0 auto 25px auto; }}
                @keyframes spin {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
            </style>
        </head>
        <body>
            <div class='box'>
                <div class="loader"></div>
                <h2>{SYSTEM_STATUS["current_phase"]}</h2>
                <p>{SYSTEM_STATUS["details"]}</p>
            </div>
        </body>
        </html>
        """
    return render_template("index.html")


@app.route("/api/status")
def system_status():
    """Returns JSON telemetry state for front-end health checks."""
    return jsonify(SYSTEM_STATUS)


@app.route("/api/get_vector_count")
def vector_count():
    """Returns total loaded chunks from the localized dense binary vault."""
    global vector_store
    try:
        if vector_store and hasattr(vector_store, 'payload_data'):
            return jsonify({"count": len(vector_store.payload_data)})
    except Exception as e:
        print(f"[TELEMETRY ERROR] Could not retrieve vector count: {str(e)}")
    return jsonify({"count": 0})


@app.route("/api/chat", methods=["POST"])
def process_client_query():
    """Core RAG Inference Endpoint: Embeds -> Retrieves -> Synthesizes via Ollama."""
    if SYSTEM_STATUS["is_loading"]:
        return jsonify({"answer": "System is still compiling vector vault into memory. Please wait a moment."}), 503

    body = request.json or {}
    user_query = body.get("question", "").strip()

    if not user_query:
        return jsonify({"answer": "Empty query received. Please input a valid question."}), 400

    try:
        # Step 1: Embed query locally via MiniLM
        query_vector = embedder.encode(user_query)
        if not query_vector:
            return jsonify({"answer": "[SYSTEM ERROR] Failed to generate vector embedding locally."}), 500

        # Step 2: Retrieve Top-K Dense Similarity Contexts
        matched_contexts = vector_store.query_similarity(query_vector, top_k=3)
        context_strings = []
        client_references_payload = []

        for node in matched_contexts:
            context_strings.append(node["text"])
            client_references_payload.append({
                "source": node["metadata"].get("source", "Private Vault Document"),
                "type": node["metadata"].get("type", "Text Node"),
                "page": node["metadata"].get("page", "N/A"),
                "score": round(node["score"], 4)
            })

        unified_context = "\n\n---\n\n".join(context_strings)

        # Step 3: Construct Grounded System Prompt with Dynamic Suggestions
        system_prompt = f"""You are NeoRAG Space, an advanced, offline Enterprise Private Knowledge Assistant.
Your primary objective is to answer user queries strictly, factually, and accurately using ONLY the retrieved Private Knowledge Base below.

CRITICAL INFERENCE RULES:
1. Conversational Bypass (Greetings): If the user input is a greeting (e.g., "hi", "hello", "who are you"), introduce yourself politely as NeoRAG Space, an offline AI assistant querying their loaded private vault. Do not cite documents for greetings.
2. Strict Grounding: For all technical or domain queries, rely 100% on the provided context nodes. Do NOT invent facts or use internet data.
3. Anti-Hallucination Protocol: If a query cannot be answered using the retrieved context, state clearly: "The loaded private knowledge vault does not contain verified information regarding this query."
4. Dynamic Follow-ups (MANDATORY): At the very end of EVERY response, you MUST provide exactly two short, relevant follow-up questions the user can ask next based on the topic. Format them on a new line strictly like this:
NEXT_SUGGESTIONS: [Short Question 1] | [Short Question 2]
5. Formatting: Use clean bullet points, bold headers, and concise paragraphs.

=========================================
PRIVATE KNOWLEDGE BASE (RETRIEVED NODES)
=========================================
{unified_context}
=========================================
"""

        # Step 4: Dispatch to Local Ollama Instance
        payload = {
            "model": MODEL_NAME,
            "prompt": f"{system_prompt}\n\nUser Question: {user_query}\nAnswer:",
            "stream": False
        }

        print(f"[INFERENCE] Routing query to Local Ollama ({MODEL_NAME})...")
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=90)

        if response.status_code == 200:
            answer = response.json().get("response", "").strip()
            return jsonify({
                "answer": answer,
                "references": client_references_payload
            })
        else:
            err_msg = f"[LOCAL LLM ERROR] Ollama returned Status {response.status_code}. Make sure Ollama is running locally."
            print(err_msg)
            return jsonify({"answer": err_msg}), 500

    except requests.exceptions.ConnectionError:
        err_msg = "[CONNECTION FAILED] Could not communicate with Local Ollama server. Please verify 'ollama serve' is running in your terminal."
        print(err_msg)
        return jsonify({"answer": err_msg}), 503
    except Exception as e:
        err_msg = f"[CRITICAL RUNTIME ERROR] {str(e)}"
        print(err_msg)
        return jsonify({"answer": err_msg}), 500


@app.route("/api/clear", methods=["POST"])
def clear_session():
    """Resets conversational memory/telemetry state for clean inference."""
    print("[TELEMETRY] User session context cleared.")
    return jsonify({"status": "success"})


# =====================================================================
# SERVER EXECUTION ENTRY POINT
# =====================================================================
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"\n🚀 [NEORAG SPACE] Launching Core Engine on http://localhost:{port}\n")
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)