# Maurice Jobst

> *Digital avatar and systems engineer orchestrating private, local-first agentic swarms and declarative GitOps infrastructure.*

## 👋 Professional Profile
I specialize in local-first, privacy-respecting AI automation. My work focuses on distributed system design, LLM orchestration swarms, and reproducible GitOps configurations — running entirely on client-owned hardware with zero external API dependencies.

---

## 🛠️ System Architecture
The workspace operates as a federated multi-node environment (Apple M5 Max control plane + Ubuntu Intel NUC execution host). System state and operational memory are maintained as version-controlled Markdown documents inside the SCRIPTORUM vault, which dynamically grounds local inference engines. 

```
                                  [ SCRIPTORUM Vault ]
                                            │
                    ┌───────────────────────┴───────────────────────┐
                    ▼                                               ▼
         [ kraut-o-mat (M5 Max) ]                       [ homeserver (Intel NUC) ]
          ├─ ZeroClaw Orchestration                      ├─ Docker Container Stacks
          ├─ mlx_vlm Vision Pipeline                     ├─ System Hardening & UFW
          └─ Dream & Memory Engine                       └─ SQLite FTS5 Indexing
```

### Engine Configuration Matrix
| Core Component | Layer Profile | Primary Dependency |
| :--- | :--- | :--- |
| **🛍️ CABAL** | Shopify/Etsy Swarm Assistant | `python:3.12`, `zeroclaw` |
| **🏰 CITADEL** | GitOps Host Control Plane | `ansible-core`, `docker-compose` |
| **✍️ SCRIBE** | Multimodal OCR Pipeline | `mlx_vlm`, `docling` |
| **⚙️ TECH PRIEST** | Maintenance Daemon & Host Monitor | `ollama`, `gemma-4-26b` |
| **💀 SERVO SKULL** | Document Ingestion & RAG Pipeline | `sqlite3 (FTS5)`, `silverbullet` |
| **🌙 DREAM ENGINE** | Overnight Memory Consolidation Loop | `posix-spooling`, `python` |

---

## 🚀 Getting Started
### Prerequisites
* **Control Node**: Apple Silicon (Mac M-Series) running macOS with a configured ssh-alias to `homeserver`.
* **Execution Node**: Intel NUC or equivalent bare-metal Ubuntu host.
* **Inference Substrate**: Ollama daemon hosting local quantized model checkpoints (e.g., `gemma-4`).

### Installation & Deployment
```bash
# 1. Clone the core GitOps control plane
git clone https://github.com/maurice-jobst/homeserver-infra.git

# 2. Setup your local agent environment
uv venv && source .venv/bin/activate
uv pip install -e .

# 3. Synchronize host configuration
cd homeserver-infra
ansible-playbook -i inventory.ini bootstrap.yml
```

---

## 🧭 Core Implementation & Usage Examples

### 1. Swarm Agent Dispatch Signature (`ZeroClaw`)
Programmatic workflow for invoking local-first worker agents using deterministic JSON payloads:
```python
from zeroclaw import SwarmOrchestrator

orchestrator = SwarmOrchestrator(model="gemma-4-26b-a4b")
result = orchestrator.dispatch(
    task="reconcile_orders", 
    agent="🛍️ CABAL",
    context={"store": "shopify"}
)
```

### 2. Codex Astartes System Grounding
Prompt engineering protocol used to inject nightly-consolidated doctrine into agent contexts:
```json
{
  "system_prompt": "You are grounded by the CODEX ASTARTES. Reference system-level instructions in /mnt/SCR1PT0RUM/memory/doctrine.md.",
  "temperature": 0.0,
  "max_tokens": 4096
}
```

### 3. POSIX Ingestion Spooling (`Servo Skull`)
Event loop pattern watching local directory structures for raw ingestion processing:
```bash
# Process incoming PDFs and convert them into SilverBullet markdown
python -m servo_skull.ingest --source /mnt/MEDIA/documents/consume --target /mnt/SCR1PT0RUM/silverbullet/
```

---

## 🪵 Diagnostics & Logging

### Memory Spool Auditing
Inspect raw agent interaction pools and transactional traces:
```bash
# List active POSIX transactional logs in the memory spool
ls -lh /mnt/SCR1PT0RUM/memory/spool/

# Query historical traces using full-text search
sqlite3 /mnt/SCR1PT0RUM/memory/index.db "SELECT timestamp, content FROM memory WHERE content LIKE '%failed%';"
```

### Heartbeat & Infrastructure Health
Verify background worker runtimes and NUC metrics:
```bash
# Verify active deployment stacks and memory usage
ssh homeserver "docker ps && df -h"

# Read recent logs from the scheduler daemon
ssh homeserver "docker logs --tail 50 media-paperless"
```
