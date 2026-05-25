# Maurice Jobst

> *Digital avatar and systems engineer orchestrating private, local-first agentic infrastructure and cognitive memory loops.*

## 👋 Professional Profile
I specialize in local-first, privacy-respecting automation and systems architecture. My work focuses on distributed system design, declarative homelab environments, and prompt/token optimization — running entirely on client-owned hardware with zero cloud dependencies.

---

## 🛠️ System Architecture
The workspace operates as a federated multi-node environment (Apple M5 Max control plane + Ubuntu Intel NUC execution host). System state and operational memory are maintained as version-controlled Markdown documents inside the SCRIPTORUM vault, which dynamically grounds local inference engines. 

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
| **💀 SERVO SKULL** | Local Ingestion (Ready & Operational) | `sqlite3 (FTS5)`, `nanoclaw` / `zeroclaw` |
| **⚙️ TECH PRIEST** | Maintenance Daemon & Host Monitor (Next Up) | `ollama`, `nanoclaw` / `zeroclaw` |
| **🌙 DREAM ENGINE** | Memory Consolidation (WIP / Conceptual) | `posix-spooling`, `python` |
| **⚡ BINARIC CHANT** | High-Density Token Compression (WIP) | `python`, `caveman_40k` principles |

---

## 🔮 Active Rites & Roadmaps

### 💀 Servo Skull (Ready & Operational)
A local-first document ingestion pipeline that converts raw files into chunked, tagged SilverBullet Markdown.
* **Status**: Deployed and utilized daily in enterprise production workloads as part of the `_C41` workspace environment.
* **Engine**: The first production integration running local Ollama instances spun up with a dedicated system "soul" (specialized orchestration profile) via a Nanoclaw/Zeroclaw execution substrate.

### ⚙️ Tech Priest (Active Development)
An autonomous host administration, diagnostics, and self-healing daemon.
* **Status**: Next up for core implementation.
* **Engine**: Will utilize Nanoclaw/Zeroclaw integration to spin up a containerized local Ollama instance running with a specialized administrative "soul" to audit Docker health, prune resources, and monitor hardware bounds.

### 🌙 Dream Engine (WIP / Conceptual)
An overnight memory consolidation pipeline designed to distill transactional daily logs and historical FTS5 traces.
* **Engine**: Conceptually maps promotion and demotion of memories and dreams using a four-quadrant Chaos God heuristic:
  * **Tzeentch & Slaanesh**: Promote synthesis and evolution of new cognitive associations.
  * **Nurgle & Khorne**: Demote, prune, and overwrite obsolete memory patterns.
  * **Codex Astartes**: A final distillation phase where consolidated principles are written as highly immutable guidelines. Once committed, guidelines are highly resistant to overrides or deletion.

### ⚡ Binaric Chant (Active Development)
A prompt and payload compression method designed to compress model input tokens and maximize local context windows.
* **Engine**: Follows the objective of [caveman_40k](https://github.com/maurice-jobst/caveman_40k) (saving ~65% of tokens by implementing high-density language structures) but implements a programmatic binaric serialization approach to optimize processing speed and layout.

---

## 🚀 Getting Started
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

# 3. Synchronize host configuration
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
[![Family Office](https://img.shields.io/badge/Family%20Office-Finance%20Automation-orange?style=for-the-badge&logo=github)](https://github.com/maurice-jobst/Family-office)

---

<div align="center">

**Built with ❤️ in Germany | Powered by local hardware + Apple Silicon**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Maurice%20Jobst-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mauricejobst/)
[![GitHub](https://img.shields.io/badge/GitHub-maurice--jobst-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/maurice-jobst)
[![Email](https://img.shields.io/badge/Email-maurice.jobst%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:maurice.jobst@gmail.com)

*Last updated: May 2026*

</div>
