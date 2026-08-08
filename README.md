<div align="center">
  <h2># 🌌 NeoRAG Space — Enterprise Local Private Knowledge Core</h2>
  <p><b>Architected by Md Salik Ubair</b></p>
  <p><i>A production-grade, 100% offline, local Retrieval-Augmented Generation (RAG) platform engineered to parse, split, vectorize, and search deep technical text repositories. Architected to eliminate data leaks to public clouds, providing seamless, real-time interactive intelligence backed by an air-gapped local computational environment.</i></p>

  <img src="https://img.shields.io/badge/Architecture-Offline_RAG-success?style=for-the-badge" alt="Architecture" />
  <img src="https://img.shields.io/badge/Frontend-HTML5_%7C_CSS3_%7C_Vanilla_JS-blue?style=for-the-badge" alt="Frontend" />
  <img src="https://img.shields.io/badge/Backend-Python_%7C_Flask-4B8BBE?style=for-the-badge" alt="Backend" />
  <img src="https://img.shields.io/badge/Database-NumPy_Binary_Vault-yellow?style=for-the-badge" alt="Database" />
  <img src="https://img.shields.io/badge/LLM-Ollama_%7C_Llama3-8A2BE2?style=for-the-badge" alt="LLM" />
  <img src="https://img.shields.io/badge/Embeddings-all--MiniLM--L6--v2-red?style=for-the-badge" alt="Embeddings" />
</div>

<br>

By leveraging decentralized Python modules combined with memory-cached NumPy matrix computations, the pipeline extracts fact-based references from academic textbooks, software manuals, and processed multimedia transcripts to constrain a local LLM runtime engine via Ollama.

---

## 🖥️ Live Production Dashboard Preview & Core Assets

### 🔍 Live System Inference & Response Attribution
The custom web client provides real-time, explainable structural analytics by linking local LLM generation directly to the source knowledge base via verifiable metadata attribution.

<div align="center">
  <img src="./assets/NeoRAG_Look.png" alt="NeoRAG Look" width="90%" />
</div>

#### Explanation of the Inference Flow:
* **Context-Aware Generation:** Upon receiving a query, the semantic tracking core automatically scans the local vector vault to extract high-dimensional nodes aligned with user inputs.
* **Granular Source Attribution:** Each response outputs an isolated **Citations Block**, detailing exact file origins (`handbook.pdf`), specific page boundaries (`Page 82`), and mathematical **Similarity Match Scores** (`76.4%`).
* **Trust & Transparency:** By exposing exact match percentages, users can independently verify the relevance and factual grounding of the AI's response against the private document corpus.
* **Real-Time Telemetry:** The dashboard monitors operational health dynamically, displaying active matrix statistics (such as **46,238 active vector nodes**) locked in the current memory matrix.

---

### ⚡ Core Operational Pipelines

| 🧠 REAL-TIME DOMAIN INFERENCE | 🔬 DATA SCIENCE CORE PIPELINE |
| :---: | :---: |
| <img src="./assets/neo_rag_response_demo.png" alt="NeoRAG Response Demo" width="100%" /> | <img src="./assets/demo_21.png" alt="Data Science Demo" width="100%" /> |
| > *Demonstrating factual query extraction and dynamic follow-up prediction chips.* | > *Showcasing Markdown code rendering, SIMD optimization docs, and Pandas structural tracing.* |

---

### 🏗️ Architecture Showcase & Branding

| 📊 PROJECT SHOWCASE (PPT VIEW) | 🚀 CORE BRANDING ASSET |
| :---: | :---: |
| <img src="./assets/NeoRAG_Architecture.png" alt="NeoRAG Architecture" width="100%" /> | <br><img src="./assets/NeoRAG_Space_Logo.ico" alt="NeoRAG Space Logo" width="180px" /><br><br> |
| > *Integrated interactive timeline detailing project origin, data engineering, and system flow.* | > *Custom executable branding platform icon.* |

---
## 🛠️ System Architecture Design & Data Pipelines

```bash
+---------------------------------------------------------------------------------+
|                    🚀 NeoRAG Space: Architecture Flow 🚀                        |
+---------------------------------------------------------------------------------+

 [ 📄 Private Documents ] (PDF, TXT, JSON Transcripts)
          │
          ▼
 [ ⚙️ 1. Ingestion Layer ] -----------> Parses streams & tracks file metadata
          │
          ▼
 [ ✂️ 2. Semantic Chunker ] ----------> Overlapping 500-char context windows
          │
          ▼
 [ 🧠 3. Local Embedder ] ------------> all-MiniLM-L6-v2 (384-dim dense tensors)
          │
          ▼
 [ 💾 4. Vector Vault (.bin) ] -------> Binary serialized NumPy storage matrix
          │
          +-----------------------+ (User Query hits Flask Backend)
                                  │
                                  ▼
 [ 🧮 5. Similarity Search ] ---------> Dot-Product & Cosine Distance math scan
                                  │
                                  ▼
 [ 🤖 6. Ollama Local LLM ] ----------> Llama3 synthesizes factual answers locally
                                  │
                                  ▼
 [ 💻 7. Client Dashboard ] ----------> Displays Response + Citation Metrics UI
```text
[Raw Private PDFs] + [Lecture JSON Transcripts] + [Plain Text Volumes]
                                    │
                                    ▼
                     [ PHASE 1: DATA INGESTION UTILITY ]
              (Extracts characters & traces unique file source strings)
                                    │
                                    ▼
                     [ PHASE 2: SEMANTIC SLIDING CHUNKER ]
               (Slices corpus into overlapping 500-char context slots)
                                    │
                                    ▼
                    [ PHASE 3: TRANSFORMER TRANSFORMATION ]
               (Maps text nodes to 384-dimensional dense tensors locally)
                                    │
                                    ▼
                     [ PHASE 4: PERSISTENT STORAGE VAULT ]
              (Serializes matrix data structures cleanly to local binary .bin)
                                    │
                                    ▼
                     [ PHASE 5: NUMPY SIMILARITY SEARCH ]
             (Computes vector dot products & Euclidean space Cosine norms)
                                    │
                                    ▼
                     [ PHASE 6: LOCAL INFERENCE RUNTIME ]
            (Asynchronous multi-threaded Flask server streaming via Ollama)
```
1. Ingestion Layer (src/ingestor.py)Multi‑format file streaming engine parsing binary data streams across page‑by‑page PDF inputs, nested JSON video transcript properties, and raw unformatted plain text logs.
2. Context Window Chunker (src/chunker.py)Implements a sliding character window algorithm splitting strings into structured blocks with predefined context balance configurations (~15% overlap) to completely avoid linguistic data clipping at node edges.
3. High‑Dimensional Transformation Engine (src/embedder.py)Loads a localized transformer framework (all‑MiniLM‑L6‑v2) directly within hardware cache spaces, executing spatial vector mappings that convert characters into a static vector field containing 384 floating‑point channels without external network calls.
4. Persistent Vector Index Database (src/vector_store.py)Handles clean memory dumping through binary serialization, locking compiled tracking payloads safely inside a high‑speed .bin disk format.
5. Numpy Mathematical Search Layer (src/vector_store.py)Employs optimized matrix mathematical operations natively to calculate vector‑space angles via the Cosine Similarity 
### formula:
### Similarity score = (Q . V) / ||Q|| ||V||
6. Asynchronous Framework Portal (app.py)Built with a multithreaded architecture. On bootup, a background worker primes the multi‑dimensional index vector payload directly into the server’s RAM while simultaneously hosting a responsive progress monitor layout in the browser to ensure zero connection timeout anomalies.
# 🗂️ Repository Blueprint & Taxonomy MappingPlaintextRAG_Master_Project/
```text 
├── .venv/                      # Isolated sandboxed environment dependencies cluster
├── assets/                     # Graphic resources and user dashboard layout preview captures
│   ├── demo_21.png              # Data science workflow and markdown rendering demonstration
│   ├── neo_rag_response_demo.png # Live operational inference attribution screenshot
│   ├── NeoRAG_Architecture.png # Integrated interactive presentation (PPT) showcase capture
│   ├── NeoRAG_Look.png         # Main executive workspace and vector matrix dashboard view
│   └── NeoRAG_Space_Logo.ico   # Custom core branding application platform asset logo
├── Knowledge_Source/           # Local data library vault (PDFs, research textbooks, text materials)
├── smart_jsons/                # Extracted multimedia transcript raw key datasets
├── src/                        # Modular Object-Oriented Logic Architecture
│   ├── __pycache__/            # Cached bytecode run-time tracking matrices
│   ├── chunker.py              # Text segmenting sliding semantic matrix window code
│   ├── embedder.py             # Feature vectors token conversion transformer blueprint
│   ├── ingestor.py             # File collection pipeline parsing raw document strings
│   ├── memory_manager.py       # Multi-turn rolling dialogue buffer arrays state system
│   └── vector_store.py         # Persistent file writing and dot-product matrix arithmetic blocks
├── templates/                  # Interface structure presentation layers
│   └── index.html              # Custom asynchronous client view template configuration
├── vault_manager/              # Compiled vector storage repositories directory
│   └── vector_index.bin        # Consolidated floating spatial database file asset
├── app.py                      # Multi-threaded Flask orchestration engine web router server
├── download_model.py           # Utility script for localized offline model caching
├── main_pipeline.py            # Master vector matrix builder compiler script execution entrypoint
├── query_engine.py             # Standalone interactive terminal prompt shell interface utility
└── requirements.txt            # System hardware-efficient library dependency specifications
```
#### 🚀 Technical Setup & Deployment SequenceFollow these engineering sequence parameters to compile and run the local private knowledge instance seamlessly:
1. Isolated Virtual Ecosystem ActivationInitialize the local tracking space and pull down the optimized operational frameworks:Bash# Initialize and activate your virtual execution environment track
.venv\Scripts\activate

# Install the hardware-efficient scientific libraries
pip install -r requirements.txt
2. Bootstrapping the Local Inference Node via OllamaEnsure the underlying background model server container boundaries are initialized:Bash
# Initialize Ollama local background model service
ollama serve
# Pull down the required base model for the target language assets locally
ollama run llama3
3. Running the Matrix Compilation Pipeline
Repopulate the vault_manager/vector_index.bin structure with any textbook or reference content, then run the master compiler script:

python main_pipeline.py
4. Spawning the Asynchronous Web Application Core
Initialize the main production server orchestration framework or double-click the standalone NeoRAG_Space.bat desktop execution launcher:

python app.py

Access the live executive dashboard at: 👉 http://127.0.0.1:5000 but in your own Personal computer.
## 📊 System Performance & Optimization Metrics

| **Component** | **Description** | **Optimization Strategy** |
| :--- | :--- | :--- |
| **Chunker** | Sliding semantic window segmentation | Balanced overlap ratio (~15%) to preserve structural boundaries |
| **Embedder** | MiniLM‑L6‑v2 transformer model | Batch embedding with local multi‑core hardware acceleration |
| **Vector Store** | Binary serialization of dense tensors | Memory‑mapped `.bin` matrix index offloading |
| **Search Layer** | NumPy cosine similarity mathematics | Vectorized dot‑product calculation loops |
| **Inference** | Flask server + Ollama local engine | Asynchronous background multithreading system |

## 🔒 Security & Governance Protocols

- **100% Air-Gapped Execution:** Zero external network dependency or cloud API processing calls; all calculations execute securely inside the local computer workspace.
- **Data Privacy Assurance:** All private PDFs, audio transcripts, and plain-text metadata logs remain securely enclosed within the localized workspace repository bounds.
- **Integrity Validation:** The vector payload layer undergoes matrix structure validation bounds checking prior to persistent binary serialization.
- **Exclusion Governance:** Heavy indices and virtual dependency arrays are completely decoupled from remote tracking trees via strict operational boundaries inside `.gitignore`.

---

## 👨‍💻 Developer & Architect

This system was solo-architected and developed from the ground up as an Enterprise Data Privacy & AIML Portfolio Module, focusing on localized mathematical computation, multi-format data engineering, and standalone software execution.

- **Developer:** Md Salik Ubair
- **Domain:** Computer Science & AIML Engineering 
- **Live Portfolio & Projects Showcase:** [portfolio-salik-live.vercel.app](https://portfolio-salik-live.vercel.app)

---
*Engineered with a focus on Zero Telemetry, Complete Data Privacy, and Standalone Edge Intelligence (2026).*
