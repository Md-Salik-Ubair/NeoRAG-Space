# 🌌 NeoRAG Space — Enterprise Local Knowledge Core

An advanced, 100% offline, privacy-centric **Retrieval-Augmented Generation (RAG)** engine engineered from scratch using Python. The system vectorizes custom raw educational assets, enterprise documentation, and processed media transcripts into a high-dimensional mathematical vector space to provide deterministic local language inference with strict zero-leakage constraints.

---

## ⚡ Core Technical Features

* **Complete Spatial Privacy:** Entire computing cluster runs locally on system memory and hardware loops. Zero external API execution pipelines or data exposure risk.
* **Optimized Matrix Search:** Vector indexes are searched using a highly efficient NumPy-optimized mathematical dot product array layer executing calculated **Cosine Similarity**.
* **Strict Parameter Control:** Configured inference boundaries at low temperature execution (`0.2`) to effectively eliminate contextual hallucinations.
* **Contextual Sliding Window:** Documents parsed utilizing structured character chunk splits (Chunk Size: `500` characters | Overlap: `100` characters) to preserve micro-semantic structures.
* **Source Attribution Matrix:** Every programmatic answer streams live with verifiable file metadata tracking, match percentages, and source citation parameters.

---

## 🛠️ Architecture Blueprint Pipeline

```text
[Local Raw Documents Input]
             │
             ▼ 
[Sliding Character Windows Text Splitter]
             │
             ▼ 
[all-MiniLM-L6-v2 Matrix Embedder Layer]
             │
             ▼ 
[7,451 High-Dimensional Floating Points Space]
             │
             ▼ (User Query Evaluation Triggered)
[NumPy Optimized Cosine Distance Core Calculations]
             │
             ▼ (Top Matching Context Node Selection)
[Ollama Llama3 8B Low-Temp Hyper-Prompt Loops]
             │
             ▼ (Asynchronous Backend Server Packaging)
[Flask API Core Endpoint Routing Stream Layout]
             │
             ▼ 
[NeoRAG Space Frontend UI Panel Live Client Render]

📁 Repository Directory Taxonomy
app.py — Core operational application controller executing server bindings and endpoint routing loops.

query_engine.py — Analytical vector computational block managing distance matrices and context packaging.

main_pipeline.py — System ingestion core parsing raw files, token streams, and array operations.

templates/index.html — Premium responsive dashboard panel designed with explicit dark theme configurations.

Knowledge_Source/ — Secure directory hosting raw engineering documentation, textbooks, and assets.

transcripts/ — Storage array containing contextual multi-turn structured dialogue transcription inputs.

smart_jsons/ — Production metadata configurations tracking high-density array reference nodes.