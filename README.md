# 🌌 NeoRAG Space — Enterprise Local Private Knowledge Core

NeoRAG Space is a production-grade, 100% offline, local Retrieval-Augmented Generation (RAG) platform engineered to parse, split, vectorize, and search deep technical text repositories. The system is architected to eliminate data leaks to public clouds, hosting complex vector spaces and multi-turn linguistic models entirely within a sandboxed local environment.

By leveraging decentralized Python modules combined with memory-cached NumPy matrix computations, the pipeline extracts fact-based references from academic textbooks, software manuals, and lecture transcripts to constrain a local LLM runtime engine via Ollama.

---

## 🖥️ Live Production Dashboard Preview & Core Assets

The architecture maps local knowledge spaces onto an ultra-premium, dark-themed responsive enterprise user interface displaying similarity match confidence metrics, dynamic reference attribution badges, and text streaming capabilities.

| 📊 CORE CLIENT INTERFACE PORTAL | 🧠 SYSTEM BRANDING ASSET |
| :---: | :---: |
| ![NeoRAG Space Desktop Client UI Panel](./assets/NeoRAG_Look.png) | ![NeoRAG Space Core Logo Engine](./assets/NeoRAG_Space_Logo.ico) |

---

## 🛠️ System Architecture Design & Data Pipelines

The system executes data transaction handling over six distinct decoupled pipeline phases on dedicated asynchronous execution layers:


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
               (Maps text nodes to 384-dimensional dense tensors via HF)
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


## ⚙️ System Architecture Overview

### 1. Ingestion Layer (`src/ingestor.py`)
Multi‑format file streaming engine parsing binary data streams across page‑by‑page PDF inputs, nested JSON video transcript properties, and raw unformatted plain text logs.

### 2. Context Window Chunker (`src/chunker.py`)
Implements a sliding character window algorithm splitting strings into structured blocks with predefined context balance configurations to completely avoid linguistic data clipping at node edges.

### 3. High‑Dimensional Transformation Engine (`src/embedder.py`)
Loads a localized transformer framework (`all‑MiniLM‑L6‑v2`) executing spatial vector mappings that convert characters into a static vector field containing 384 floating‑point channels.

### 4. Persistent Vector Index Database (`src/vector_store.py`)
Handles clean memory dumping through binary serialization, locking compiled tracking payloads safely inside a high‑speed `.bin` disk format.

### 5. Numpy Mathematical Search Layer (`src/vector_store.py`)
Employs optimized matrix mathematical operations natively to calculate vector‑space angles via the **Cosine Similarity** formula:



\[
\text{Similarity Score} = \frac{Q \cdot V}{\|Q\| \|V\|}
\]



### 6. Asynchronous Framework Portal (`app.py`)
Built with multithreaded architecture. On bootup, a background worker primes the 15,860 multi‑dimensional index vector payload directly into the server’s RAM while simultaneously hosting a glassmorphism progress monitor layout in the browser to ensure zero connection timeout anomalies.

---

## 🧠 Runtime Execution & Local Knowledge Retrieval
[User Query Input] ──► [Semantic Chunk Retrieval] ──► [Vector Similarity Search] ──► [Contextual Response Generation]

## Query Engine Initialization
Activate the interactive terminal shell interface for real-time question-answering and document retrieval:

#### Bash :
python query_engine.py

# Repository Blueprint & Taxonomy Mapping

RAG_Master_Project/
├── .venv/                      # Isolated sandboxed environment dependencies cluster
├── assets/                     # Graphic resources and user dashboard layout preview captures
│   ├── NeoRAG_Look.jpg         # Live operational responsive view interface screenshot
│   └── NeoRAG_Space_Logo.jpg   # Custom core branding application platform asset logo
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
│   └── vector_index.bin        # Consolidated 15,860-node floating spatial database file asset
├── app.py                      # Multi-threaded Flask orchestration engine web router server
├── main_pipeline.py            # Master vector matrix builder compiler script execution entrypoint
└── query_engine.py             # Standalone interactive terminal prompt shell interface utility

# 🚀 Technical Setup & Deployment Sequence
###### Follow these engineering sequence parameters to compile and run the local private knowledge instance seamlessly:

### 1. Isolated Virtual Ecosystem Activation
Initialize the local tracking space and pull down the optimized operational frameworks:

#### Bash :
# Initialize your virtual execution environment track
.venv\Scripts\activate

# Install the hardware-efficient scientific libraries
pip install pypdf sentence-transformers numpy flask requests

### 2. Bootstrapping the Local Inference Node via Ollama
Ensure the underlying background model server container boundaries are initialized:

##### Bash
# Initialize Ollama local background model service
ollama serve

# Pull down the required base model for the target language assets locally
## ollama run llama3
### 3. Running the Matrix Compilation Pipeline
###### Repopulate the vault_manager/vector_index.bin structure with any textbook or reference content, then run the master compiler script:

##### Bash
python main_pipeline.py

### 4. Spawning the Asynchronous Web Application Core
###### Initialize the main production server orchestration framework:

##### Bash
python app.py
Access the live dashboard at: 👉 http://127.0.0.1:5000

## 📊 System Performance & Optimization Metrics

| **Component** | **Description** | **Optimization Strategy** |
|----------------|-----------------|----------------------------|
| **Chunker** | Sliding semantic window segmentation | Balanced overlap ratio (~15%) to preserve edges |
| **Embedder** | MiniLM‑L6‑v2 transformer model | Batch embedding with local multi‑core acceleration |
| **Vector Store** | Binary serialization of dense tensors | Memory‑mapped `.bin` matrix index offloading |
| **Search Layer** | NumPy cosine similarity mathematics | Vectorized dot‑product calculation loops |
| **Inference** | Flask server + Ollama local engine | Asynchronous background multithreading system |

## 🔒 Security & Governance Protocols

- **Local‑Only Execution:** Zero external network dependency or cloud API processing calls; all calculations execute securely inside the local computer workspace.

- **Data Privacy Assurance:** All private PDFs, transcripts, and plain‑text metadata logs remain securely enclosed within the localized workspace repository bounds.

- **Integrity Validation:** The vector payload layer undergoes matrix structure validation bounds checking prior to persistent binary serialization.

- **Exclusion Governance:** Heavy indices and virtual dependency arrays are completely decoupled from remote tracking trees via strict operational boundaries inside `.gitignore`.


# Local Environment Registry Exclusions
.venv/
__pycache__/
src/__pycache__/
vault_manager/vector_index.bin

#### Engineered and Developed as a Solo Standalone System Platform by Md Salik Ubair — Computer Science & AIML Portfolio Module (2026)
