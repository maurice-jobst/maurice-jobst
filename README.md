# Maurice Jobst

**Principal Systems Architect & Local-First AI Engineer** | Specialist in Sovereign B2B & B2G Architectures | Guardian of the Scriptorum

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Maurice%20Jobst-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/mauricejobst/)
[![GitHub](https://img.shields.io/badge/GitHub-maurice--jobst-181717?style=flat&logo=github)](https://github.com/maurice-jobst)
![Status](https://img.shields.io/badge/Status-Systems%20Operational-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)

---

## 🏛️ Sovereign Engineering: Local-First AI for B2B & B2G
I design and deploy secure, air-gapped, and privacy-preserving automation systems. My focus is on distributed systems, local-first LLM orchestrations, high-fidelity prompt compression pipelines, and idempotent infrastructure provisioning.

### Systems Philosophy
By mapping technical states to highly structured semantic schemas (e.g. priors and canons), we anchor LLM reasoning to predictable, low-latency, and audit-compliant patterns. This hybrid approach enables enterprise-grade accuracy, massive context cost reductions, and absolute data sovereignty—ideal for highly regulated B2B and public sector (B2G) deployments.

---

## 🛠️ The Forge: Sovereign Noosphere Architecture
The workspace operates as a federated two-node environment combining an Apple M-series Silicon control plane (`kraut-o-mat`) and a bare-metal Ubuntu host (`homeserver`), aligned dynamically via **GitOps**: code moves by git, never by file-sync, and every change round-trips through a version-controlled control plane before it touches the substrate.

```
                                  [ SCRIPTORUM Vault ]
                                            │
                    ┌───────────────────────┴───────────────────────┐
                    ▼                                               ▼
          [ kraut-o-mat (M5 Max) ]                       [ homeserver (Intel NUC) ]
           ├─ Agentic Orchestration (Claude · zeroclaw)   ├─ Isolated Docker Stacks (3 networks)
           ├─ MLX-accelerated Ollama (Apple Silicon)      ├─ System Hardening & UFW
           ├─ C⁴¹ TCAI Synthesis (Codices)                ├─ Private Gitea Origin + SQLite FTS5
           └─ Binaric Chant (Token Compression)           └─ Dream Engine (4-quadrant consolidation)
```

### Core Production Components

| Component | Architecture | Production State / Dependency | B2B/B2G Value |
| :--- | :--- | :--- | :--- |
| **🏰 CITADEL** | GitOps Host Control Plane | Deployed: `ansible-core`, `docker-compose`, `sops`+`age`, `gitea` | Immutable, repeatable system setups with **age-encrypted secrets committed in-repo** (the key never leaves the control plane) and a sovereign private git origin. |
| **💀 SERVO SKULL** | Layout-Purifying Document Ingestion | Deployed: `sqlite3 (FTS5)`, `pymupdf4llm`, `markitdown` | Structural chunking and fast local semantic retrieval for sovereign document vaults. |
| **⚡ BINARIC CHANT** | Three-tier symbolic compression: Saga → Caveman → Glyph | **v0.1.0 Operational**: `python`, `transformers`, `tenacity` | **65%+ token savings** and cryptographically sealed prompt verification. |
| **⚙️ TECH PRIEST** | Autonomous Maintenance Daemon | Under active construction: `python`, `ollama` | Self-healing container environments and automated resource cleanup. |
| **🌙 DREAM ENGINE** | 4-Quadrant Codex → BDD Backlog Synthesis (CITADEL-hosted) | Design spec finalized: `posix-spooling`, `sqlite`; consumes C⁴¹ codices | Promotion/demotion of rules across Chaos God quadrants distills domain codices into sprint-ready BDD backlogs. |
| **🔬 C⁴¹ TCAI** | Deterministic synthesis engine (extract → ground → markdown → editorial codex) | **v1.1.0 Operational**: `python`, `uv`, `ollama`, `pydantic` | Federation upstream: produces domain codices (e.g., debt-recovery v1.1 — 33 rules) for downstream CITADEL Dream Engine consumption. |

### The Citadel-Pattern: 2026 Home-Ops Doctrine
The substrate is deliberately **disposable** — all authority lives on the control plane, so the NUC can be rebuilt from git at any time:

- **GitOps over file-sync** — code is moved by git only; cloud file-sync never touches a working tree (a hard-won lesson after sync conflict-copies corrupted a repo's loose objects).
- **Encrypted secrets in-repo** — `sops`+`age` keep service credentials version-controlled and reproducible; decryption happens only on the control plane, never on the substrate.
- **Sovereign private origin** — a self-hosted **Gitea** holds confidential and large-footprint repos behind the homelab boundary; public showcase work mirrors to GitHub.
- **Mac-as-code** — the workstation itself is reproducible via `chezmoi` + a `Brewfile`, so a fresh machine bootstraps to a known-good state.
- **Single sync provider per zone** — code is local, docs are single-provider, cold/binary data is archived; no folder is ever synced by two providers at once.

---

## 📦 Open-Source Implementations

### ⚡ [binaric-chant](https://github.com/maurice-jobst/binaric-chant)
A Python prompt-compression library and Click-based ratification suite:
* **Mechanism**: Compresses input through a three-tier pipeline — narrative matching to canonical Sagas, Caveman phrase compaction, and Glyph lexical substitutions.
* **SEAL Security**: Appends a cryptographically signed block carrying a SHA-256 integrity hash, a canary echo prompt for tamper detection, and a forge band certifying model and sampling provenance.
* **Status**: **Fully operational (v0.1.0)** — 27-test validation suite with automated rule-syncing.

### 💀 [servo-skull](https://github.com/maurice-jobst/servo-skull)
A layout-preserving document ingestion engine:
* **Mechanism**: Extracts textual data from complex PDFs, HTML, and Office documents with layout preservation (integrating PyMuPDF and Microsoft MarkItDown), chunking text into an optimized FTS5 database grounding.
* **Status**: Deployed and active across workspace modules.

### 🪨 [caveman_40k](https://github.com/maurice-jobst/caveman_40k)
A Claude Code skill that compresses prompts by rewriting them into a high-density "caveman" register:
* **Mechanism**: Strips function words and redundant grammar while preserving semantic load — the empirical precursor to the Caveman tier in the Binaric Chant pipeline.
* **Result**: ~65% token reduction on suitable inputs.

---

## 🔒 Proprietary Systems
*Private repositories — architecture walkthroughs and demos available on request.*

### 🔬 C⁴¹ TCAI — Deterministic Synthesis Engine
The federation's deterministic-first synthesis pipeline:
* **Mechanism**: Three-stage pipeline (extract → ground → markdown) producing high-fidelity domain codices from heterogeneous source documents, with editorial codex curation enforcing three machine-checkable invariants (regex compliance, source-cite coverage, section presence).
* **Federation contract**: C⁴¹ does deterministic synthesis and terminates at the codex; CITADEL's Dream Engine consumes the codex for 4-quadrant backlog generation.
* **Status**: **v1.1.0 Released** — debt-recovery domain codex (33 rules, 5 sections) shipped with a full operational runbook.

### 🏰 CITADEL (homeserver-infra) — GitOps Control Plane
Ansible + Docker GitOps for a hardened homelab substrate:
* **Mechanism**: Idempotent bare-metal hardening, network partitioning, and isolated container stacks hosting local Ollama, FTS5 nodes, and private services — reconciled from a single control plane with encrypted secrets.
* **Status**: Operational, orchestrating distributed system states.

### 🚃 Transit Fare-Payment Architecture *(client engagement — confidential)*
Integration models for contactless transit-payment infrastructures aligned with **Visa Contactless Transit (MTT)** and **Mastercard Transit** implementation guidelines. Delivered as a structured, version-controlled feature backlog and technical specification set. *(Client-confidential; not public.)*

---

## ✙ Active Construction Tasks

- [x] **[Chant-Task-001]** Implement core three-tier compression pipeline and regex preservers.
- [x] **[Chant-Task-002]** Implement three-band SEAL validation and heresy detection.
- [x] **[Chant-Task-003]** Implement CLI and Scriptorum logging.
- [ ] **[Priest-Task-001]** Technical implementation of autonomous self-healing loops for local daemon processes.
- [ ] **[Dream-Task-001]** Implement sqlite-based 4-quadrant (Tzeentch/Slaanesh/Nurgle/Khorne) consolidation in CITADEL, consuming C⁴¹ codices (federation handoff 2026-05-28).

---

## 🚀 Sovereign Infrastructure: The GitOps Flow
The control-plane repository is **private** (architecture walkthrough available on request). The reconciliation shape:

```bash
# 1. Control plane decrypts secrets locally — the age key never leaves the Mac
sops -d docker/<stack>/secrets.enc.env > docker/<stack>/.env

# 2. Reconcile the substrate from version-controlled state
./deploy.sh                                  # rsync config + docker compose up -d
ansible-playbook -i inventory.ini bootstrap.yml   # idempotent host provisioning
```

* **Control Node**: macOS workstation (Apple Silicon) with passwordless SSH to `homeserver`.
* **Execution Node**: Intel NUC / Ubuntu bare-metal.
* **Inference Substrate**: MLX-accelerated Ollama hosting local quantized models (e.g. `gemma4`).

---

<div align="center">

**Built with dedication | Powered by local hardware & Apple Silicon**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Maurice%20Jobst-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mauricejobst/)
[![GitHub](https://img.shields.io/badge/GitHub-maurice--jobst-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/maurice-jobst)
[![Email](https://img.shields.io/badge/Email-maurice.jobst%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:maurice.jobst@gmail.com)

*Last updated: 29 May 2026 — Citadel-pattern hardening: SOPS+age encrypted secrets, private Gitea origin, MLX-Ollama, Mac-as-code*

</div>
