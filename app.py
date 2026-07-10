import os
import sys
import threading
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from src.vector_store import LocalVectorStore
from src.embedder import TextEmbedder

load_dotenv()

app = Flask(__name__)

# Initialize Groq Client
groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

MODEL_NAME = "llama-3.3-70b-versatile"

SYSTEM_STATUS = {
    "is_loading": True,
    "current_phase": "SYSTEM_BOOT_INITIALIZATION",
    "details": "Initializing Enterprise Knowledge Intelligence Platform..."
}

VECTOR_DB_FILE = "./vault_manager/vector_index.bin"

vector_store = None
embedder = None


def async_pipeline_compilation():
    global vector_store
    global embedder
    global SYSTEM_STATUS

    try:
        SYSTEM_STATUS["current_phase"] = "API_GATEWAY_INITIALIZATION"
        SYSTEM_STATUS["details"] = "Connecting to Hugging Face Cloud Inference API..."

        # Now initializes the lightweight cloud embedder (Zero RAM load)
        embedder = TextEmbedder(model_name="sentence-transformers/all-MiniLM-L6-v2")

        SYSTEM_STATUS["current_phase"] = "VECTOR_DATABASE_LOADING"
        SYSTEM_STATUS["details"] = "Loading indexed knowledge base into memory..."

        vector_store = LocalVectorStore(storage_file=VECTOR_DB_FILE)
        vector_store.load_index()

        SYSTEM_STATUS["current_phase"] = "SYSTEM_READY"
        SYSTEM_STATUS["details"] = "Enterprise Knowledge Platform Ready. Zero Local RAM footprint achieved."
        SYSTEM_STATUS["is_loading"] = False

        print("[SYSTEM READY] Cloud-based RAG architecture is fully operational.")

    except Exception as e:
        SYSTEM_STATUS["current_phase"] = "BOOT_FAILED"
        SYSTEM_STATUS["details"] = f"CRITICAL ERROR: {str(e)}"
        print(f"[BOOT FAILED] {str(e)}")


threading.Thread(
    target=async_pipeline_compilation,
    daemon=True
).start()


@app.route("/")
def home():
    if SYSTEM_STATUS["is_loading"]:
        # Upgraded premium loading screen for enterprise feel
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="refresh" content="2">
            <style>
                body {{ background: #070b13; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; font-family: 'Inter', sans-serif; margin: 0; }}
                .box {{ width: 500px; text-align: center; padding: 40px; background: #101826; border: 1px solid #26364e; border-radius: 16px; box-shadow: 0 15px 45px rgba(0,0,0,.35); }}
                h2 {{ color: #38bdf8; margin-bottom: 15px; font-weight: 700; }}
                p {{ color: #cbd5e1; font-size: 15px; }}
                .loader {{ border: 4px solid rgba(255,255,255,0.05); border-top: 4px solid #3b82f6; border-radius: 50%; width: 40px; height: 40px; animation: spin 1s linear infinite; margin: 0 auto 25px auto; }}
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


@app.route("/api/get_vector_count")
def vector_count():
    global vector_store
    try:
        if vector_store and hasattr(vector_store, 'payload_data'):
            return jsonify({
                "count": len(vector_store.payload_data)
            })
    except:
        pass
    return jsonify({"count": 0})


@app.route("/api/chat", methods=["POST"])
def process_client_query():
    if SYSTEM_STATUS["is_loading"]:
        return jsonify({
            "answer": "Knowledge Base is still loading. Please wait."
        }), 503

    body = request.json or {}
    user_query = body.get("question", "").strip()

    if not user_query:
        return jsonify({
            "answer": "Empty query."
        }), 400

    try:
        # HUGE CHANGE HERE: Using the updated cloud embedder logic safely
        query_vector = embedder.encode(user_query)
        
        if not query_vector:
            return jsonify({
                "answer": "[SYSTEM ERROR] Failed to generate vector from Cloud API. Ensure HF_API_KEY is correct."
            }), 500

        matched_contexts = vector_store.query_similarity(
            query_vector,
            top_k=3
        )
        
        context_strings = []
        client_references_payload = []

        for node in matched_contexts:
            context_strings.append(node["text"])
            client_references_payload.append({
                "source": node["metadata"].get("source", "Unknown"),
                "type": node["metadata"].get("type", "Unknown"),
                "page": node["metadata"].get("page", "N/A"),
                "score": round(node["score"], 4)
            })

        unified_context = "\n\n".join(context_strings)

        system_prompt = f"""
You are NeoRAG Space.
An Enterprise Private Knowledge Intelligence Assistant.
Your primary responsibility is to answer ONLY using the retrieved private knowledge context.

Rules:
1. Never pretend to search the internet.
2. If the answer exists inside the retrieved knowledge, answer confidently.
3. If the retrieved knowledge is insufficient, clearly state that the uploaded knowledge base does not contain enough verified information.
4. Do not fabricate facts.
5. Keep answers professional, well structured, easy to read.

============================
PRIVATE KNOWLEDGE BASE
{unified_context}
============================
"""
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            temperature=0.3,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ]
        )

        answer = completion.choices[0].message.content.strip()

        return jsonify({
            "answer": answer,
            "references": client_references_payload
        })

    except Exception as e:
        return jsonify({
            "answer": f"[SERVER ERROR] {str(e)}"
        }), 500


@app.route("/api/clear", methods=["POST"])
def clear_session():
    return jsonify({"status": "success"})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)