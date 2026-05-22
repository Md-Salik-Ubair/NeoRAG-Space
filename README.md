# 🌌 NeoRAG Space — Enterprise Local Knowledge Core

An advanced, 100% offline, privacy-centric **Retrieval-Augmented Generation (RAG)** engine engineered from scratch using Python. The system vectorizes custom raw educational assets, enterprise documentation, and processed media transcripts into a high-dimensional mathematical vector space to provide deterministic local language inference with strict zero-leakage constraints.

---

## 📄 SYSTEM DOCUMENTATION DIRECT DOWNLOAD

📥 **Click here to view the complete framework manual:** [SYSTEMS ENGINEERING ARCHITECTURE MANUAL.pdf](SYSTEMS%20ENGINEERING%20ARCHITECTURE%20MANUAL.pdf)

---

## ⚡ Core Technical Features

* **Complete Spatial Privacy:** Entire computing cluster runs locally on system memory and hardware loops. Zero external API execution pipelines or data exposure risk.
* **Optimized Matrix Search:** Vector indexes are searched using a highly efficient NumPy-optimized mathematical dot product array layer executing calculated **Cosine Similarity**.
* **Strict Parameter Control:** Configured inference boundaries at low temperature execution (`0.2`) to effectively eliminate contextual hallucinations.
* **Contextual Sliding Window:** Documents parsed utilizing structured character chunk splits (Chunk Size: `500` characters | Overlap: `100` characters) to preserve micro-semantic structures.
* **Source Attribution Matrix:** Every programmatic answer streams live with verifiable file metadata tracking, match percentages, and source citation parameters.

---

## 🖼️ System Interface & Execution Workstation

### 1. Production Web Dashboard Interface
The live operational client-side dark UI workstation managing user queries, metadata responses, and source citation metrics.

![NeoRAG Space Desktop Interface Workstation](neorag_look.png)

### 2. Desktop System Shortcut Integration
The system launcher deployment optimized with a custom application icon identity footprint.

![System Desktop Shortcut Launcher](NeoRAG_Space_Logo.ico)

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

💻 Codebase Compilation Architecture & Directory Taxonomy
The local structural alignment layout managing sub-modules, core operational dependencies, and system repository directory tracking files:

app.py — Operational application orchestration engine and API route manager.

query_engine.py — Advanced analytical mathematical matrix computing core running the optimized local NumPy Engine.

main_pipeline.py — System ingestion pipeline handler executing sliding character window document tokenization loops.

read_chunks.py — Internal data debugging module validating vectorized high-dimensional embedding tracking indices.

.gitignore — Security tracking interceptor layer protecting repository against staging local or binary data cloud dump.

README.md — Visual production portfolio index providing system architecture blueprints and runtime guidelines online.

SYSTEMS ENGINEERING ARCHITECTURE MANUAL.pdf — Full comprehensive printable systems engineering and documentation manual.

templates/index.html — Dark-theme premium UI workspace web panel dashboard implementing rolling context session buffers.