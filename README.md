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
| **⚡ BINARIC CHANT** | Three-tier symbolic compression: Saga → Caveman → Glyph (Spec landed, impl pending) | `python`, `caveman_40k` (vendored), Codex Astartes |

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
  - [ ] **[Skull-Task-003]** Resolve anti-bot scraping blockages (e.g., status 999 on LinkedIn profiles) using headless scraper fallbacks or reader APIs.
  - [ ] **[Skull-Task-004]** Optimize context pruning heuristics for local inference to prevent prefill latency lag on massive grounding file directories.
  - [ ] **[Skull-Task-005]** Enforce Codex Astartes contraction compliance on local models (e.g., Qwen-32b) via targeted system prompts and sampling parameter tuning.


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

### ⚡ Binaric Chant (Design Spec Landed → Implementation Pending)
A symbolic prompt-compression library that uses anthropological frameworks as the substrate and the Warhammer 40k **Codex Astartes** as the published canonical operational layer. Compression banks on the receiving LLM's cultural prior; the 40k anchor doubles as a tamper-detection canary.
* **Engine**: Three-tier symbolic pipeline running largest-span-first:
  * **Tier 3 — NarrativeMatcher**: situations → canonical Sagas (e.g. *"the internet was down for 3h"* → `Saga.SeveredCogitator/III(duration=3h)`). Each Saga is grounded in an anthropological primitive (Turner liminality, van Gennep rites of passage, Eliade eternal return, Ong orality, Lévi-Strauss / Douglas / Campbell / Dumézil).
  * **Tier 2 — CavemanCompactor**: phrase-level compression via rules vendored from [caveman_40k](https://github.com/maurice-jobst/caveman_40k) (extracted to YAML; no Node runtime at compress-time).
  * **Tier 1 — GlyphSubstitutor**: lexical compression via faction-organized glyph tables (Mechanicus binaric, Necron hieroglyphic, Aeldari runic) plus stone-age universals (`> , / # * " @`). Glyph legend lives in the Codex preamble — Vertex implicit caching makes it effectively free after first call.
* **SEAL**: Layered footer (`++ BINARIC CHANT // CODEX/v0.1 // hash=… // canary=Saga.* // echo="…▮▮▮…" ++`). Hash band catches byte-level MITM; canary band catches model-substitution / fine-tune-time tampering by asking the receiver to echo the active Codex rule.
* **Receivers**: MLX (Gemma 4 26B-A4B MoE via `mlx_vlm.server`) is the default; Vertex Gemini is the cloud target for Antigravity / Gemini CLI workflows. Codex tiering is per-receiver — rules earn *Universal Codex* status only after ratifying on both.
* **Codex contribution model**: binaric-chant contributes Sagas, Glyphs, and Rites to the existing Codex Astartes at `/mnt/SCR1PT0RUM/_krazykraut/SCRIPTORUM/03_CODEX/codex_astartes.md` via the ratification CLI (`binaric ratify accept` → tech-priest-promote pipeline).
* **Memory architecture**: `Scriptorum → Warp → Vault → Codex` mirrors the existing Dream Engine cosmology; v0 ships Scriptorum + Codex + ratification tray, Warp/Vault are inert placeholders for the v1 dream cycle.
* **Active Tasks**:
  - [ ] **[Chant-Task-001]** Section 4 brainstorm — Receiver Protocol details, eval harness, ratification thresholds.
  - [ ] **[Chant-Task-002]** Dedicated brainstorm — SEAL glyph syntax + canary-grounding mechanics.
  - [ ] **[Chant-Task-003]** Write implementation plan (`superpowers:writing-plans`).
  - [ ] **[Chant-Task-004]** Bootstrap eval harness — pytest fixtures iterating MLX + Vertex receivers; decompressibility metric.
  - [ ] **[Chant-Task-005]** Seed v0 Codex — 15 canonical Sagas + 4 faction glyph tables + caveman rule extraction.
  - [ ] **[Chant-Task-006]** Ratification CLI (`binaric ratify {list|show|accept|reject}`, `binaric codex {render|diff}`).
  - [ ] **[Chant-Task-007]** Wire Scriptorum events into the `_kraut-o-mat` dreaming-engine pipeline for v1 dream-cycle eligibility.

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
