# Maurice Jobst

**Systems Architect & Tech-Priest** | Guardian of the Scriptorum | Local-First AI Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Maurice%20Jobst-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/mauricejobst/)
![Architecture](https://img.shields.io/badge/Architecture-Distributed%20Local%20AI-brightgreen)
![Status](https://img.shields.io/badge/Status-Active%20Development-blue)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)

---

## 👋 Gnostic Cognitive Engineering
I design and operate local-first, privacy-respecting automation and systems architectures. My focus is on distributed systems, declarative homelab environments, and prompt/token optimization.

### The Philosophy
This workspace implements a gnostic and theological framework for local LLMs. By mapping technical parameters (role profiles, memory curations, and constraints) to religious, dogmatic, and mythological structures, we leverage the model's pre-trained patterns on scriptural text. This approach utilizes the LLM's latent weights for high-fidelity information preservation and rule compliance, increasing execution intelligence and efficiency.

---

## 🛠️ The Forge: Distributed Noosphere Architecture
The workspace operates as a federated multi-node environment (Apple M5 Max control plane `kraut-o-mat` + Ubuntu Intel NUC execution host `homeserver`). System states and operational memory are maintained as version-controlled Markdown documents inside the SCRIPTORUM vault, which dynamically grounds local inference engines. 

```
                                  [ SCRIPTORUM Vault ]
                                            │
                    ┌───────────────────────┴───────────────────────┐
                    ▼                                               ▼
         [ kraut-o-mat (M5 Max) ]                       [ homeserver (Intel NUC) ]
          ├─ Token Optimization & Coding                 ├─ Docker Container Stacks
          ├─ Nanoclaw / Zeroclaw Orchestration           ├─ System Hardening & UFW
          └─ Dream & Memory Engine                       └─ SQLite FTS5 Indexing
```

### Engine Configuration Matrix
| Core Component | Layer Profile | Primary Dependency |
| :--- | :--- | :--- |
| **🏰 CITADEL** | GitOps Host Control Plane | `ansible-core`, `docker-compose` |
| **💀 SERVO SKULL** | Local Ingestion & Indexing Engine | `sqlite3 (FTS5)`, `pymupdf4llm`, `markitdown`, `pypdf` (fallback) |
| **⚙️ TECH PRIEST** | Maintenance Daemon & Host Monitor (Next Up) | `ollama`, `nanoclaw` / `zeroclaw` |
| **🌙 DREAM ENGINE** | Memory Consolidation (WIP / Conceptual) | `posix-spooling`, `python` |
| **⚡ BINARIC CHANT** | High-Density Token Compression (WIP) | `python`, `caveman_40k` principles |

---

## ✙ Sanctioned Rites & Active Construction Tasks (To-Do)
We welcome contributions to the Forge. Check the following list of active engineering tasks to help optimize our stack:

### 💀 Servo-Skull (Ready & Operational)
A layout-preserving local document ingestion and FTS5 indexing engine that converts raw documents into chunked, tagged, and queryable Markdown.
* **Status**: Deployed and modularized across workspace engines (`_LinkedIn` and `_ContentForge`).
* **Engine**: Incorporates dynamic layout-purifying nodes (integrating `pymupdf4llm` with automatic `pypdf` fallback, and Microsoft `markitdown` for Office/HTML formats) and FTS5 SQLite database groundings. Equipped with automated Ansible and Docker GitOps deployment playbooks for homeserver/Citadel integration.
* **Active Tasks**:
  - [ ] **[Skull-Task-001]** Implement support for batch OCR processing using MLX vision models.
  - [ ] **[Skull-Task-002]** Optimize chunking heuristics to better identify structural layout markers in documents.

### ⚙️ Tech Priest (Active Development)
An autonomous host administration, diagnostics, and self-healing daemon.
* **Status**: Next up for core implementation.
* **Engine**: Will utilize Nanoclaw/Zeroclaw integration to spin up a containerized local Ollama instance running with a specialized administrative "soul" to audit Docker health, prune resources, and monitor hardware bounds.
* **Active Tasks**:
  - [ ] **[Priest-Task-001]** Write the orchestration loop using `nanoclaw` to bind Ollama context.
  - [ ] **[Priest-Task-002]** Develop the system-health parsing skills (handling disk space, container restarts, log pruning).

### 🌙 Dream Engine (WIP / Conceptual)
An overnight memory consolidation pipeline designed to distill transactional daily logs and historical FTS5 traces.
* **Engine**: Conceptually maps promotion and demotion of memories and dreams using a four-quadrant Chaos God heuristic:
  * **Tzeentch & Slaanesh**: Promote synthesis and evolution of new cognitive associations.
  * **Nurgle & Khorne**: Demote, prune, and overwrite obsolete memory patterns.
  * **Codex Astartes**: A final distillation phase where consolidated principles are written as highly immutable guidelines. Once committed, guidelines are highly resistant to overrides or deletion.
* **Active Tasks**:
  - [ ] **[Dream-Task-001]** Define the sqlite memory ingestion schema.
  - [ ] **[Dream-Task-002]** Map the scoring heuristics for the promotion/demotion matrix.

### ⚡ Binaric Chant (Active Development)
A prompt and payload compression method designed to compress model input tokens and maximize local context windows.
* **Engine**: Follows the objective of [caveman_40k](https://github.com/maurice-jobst/caveman_40k) (saving ~65% of tokens by implementing high-density language structures) but implements a programmatic binaric serialization approach to optimize processing speed and layout.
* **Active Tasks**:
  - [ ] **[Chant-Task-001]** Implement parser script for converting plain text to binaric chant syntax.
  - [ ] **[Chant-Task-002]** Benchmark token savings vs compression loss on local Ollama models.

---

## 🚀 Enacting the Noctilith Decree
### Prerequisites
* **Control Node**: macOS workstation (Apple Silicon) with SSH key access to `homeserver` (passwordless, alias configured in `~/.ssh/config`).
* **Execution Node**: Intel NUC or equivalent bare-metal Ubuntu host.
* **Inference Substrate**: Ollama daemon hosting local quantized model checkpoints (e.g., `gemma-4`).

### Installation & Deployment
```bash
# 1. Clone the core GitOps control plane
git clone https://github.com/maurice-jobst/homeserver-infra.git

# 2. Setup your local agent environment
uv venv && source .venv/bin/activate

# 3. Reconcile systems by running the bootstrap tasks
cd homeserver-infra
ansible-playbook -i inventory.ini bootstrap.yml
```

---

## 🧭 Usage & Diagnostics

### 1. Ingestion Event Loop (`Servo Skull`)
Event loop processing incoming PDFs and generating indexed markdown:
```bash
python -m servo_skull.ingest --source /mnt/MEDIA/documents/consume --target /mnt/SCR1PT0RUM/silverbullet/
```

### 2. Full-Text Memory Queries
Inspect the transactional traces harvested from agent memory:
```bash
# Query historical records using full-text search
sqlite3 /mnt/SCR1PT0RUM/memory/index.db "SELECT timestamp, content FROM memory WHERE content MATCH 'anomaly';"
```

---

## 📌 Featured Repositories

[![homeserver-infra](https://img.shields.io/badge/homeserver--infra-GitOps%20Control%20Plane-red?style=for-the-badge&logo=github)](https://github.com/maurice-jobst/homeserver-infra)
[![caveman_40k](https://img.shields.io/badge/caveman__40k-Token%20Compressor-blue?style=for-the-badge&logo=github)](https://github.com/maurice-jobst/caveman_40k)
[![servo-skull](https://img.shields.io/badge/servo--skull-Scoping%20Engine-purple?style=for-the-badge&logo=github)](https://github.com/maurice-jobst/servo-skull)

---

<div align="center">

**Built with ❤️ in Germany | Powered by local hardware + Apple Silicon**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Maurice%20Jobst-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mauricejobst/)
[![GitHub](https://img.shields.io/badge/GitHub-maurice--jobst-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/maurice-jobst)
[![Email](https://img.shields.io/badge/Email-maurice.jobst%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:maurice.jobst@gmail.com)

*Last updated: May 2026 (Servo Skull modular tuning)*

</div>
