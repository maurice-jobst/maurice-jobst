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
The workspace operates as a federated multi-node environment combining edge computing (Apple M-series Silicon control plane `kraut-o-mat`) and bare-metal Ubuntu hosts (`homeserver`), aligned dynamically via GitOps and structured memory pools.

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

### Core Production Components

| Component | Architecture | Production State / Dependency | B2B/B2G Value |
| :--- | :--- | :--- | :--- |
| **🏰 CITADEL** | GitOps Host Control Plane | Deployed: `ansible-core`, `docker-compose` | Immutable, repeatable system setups with zero manual configuration. |
| **💀 SERVO SKULL** | Layout-Purifying Document Ingestion | Deployed: `sqlite3 (FTS5)`, `pymupdf4llm`, `markitdown` | Structural chunking and fast local semantic retrieval for sovereign document vaults. |
| **⚡ BINARIC CHANT** | Three-tier symbolic compression: Saga → Caveman → Glyph | **v0.1.0 Operational**: `python`, `transformers`, `tenacity` | **65%+ token savings** and cryptographically sealed prompt verification. |
| **⚙️ TECH PRIEST** | Autonomous Maintenance Daemon | Under active construction: `ollama`, `nanoclaw` | Self-healing container environments and automated resource cleanup. |
| **🌙 DREAM ENGINE** | Heuristic Memory Consolidation | Design spec finalized: `posix-spooling`, `sqlite` | Long-term distillation of transactional logs into structured operational guidelines. |

---

## 📦 Key Repositories & Implementations

### ⚡ [binaric-chant](https://github.com/maurice-jobst/binaric-chant)
An advanced Python prompt-compression library and Click-based ratification suite:
* **Mechanism**: Compresses input text through a three-tier pipeline: Narrative matching to canonical Sagas, Caveman phrase compaction, and Glyph lexical substitutions.
* **SEAL Security**: Appends a cryptographically signed signature block carrying a SHA-256 integrity hash, a canary echo prompt for TAMPER detection, and a forge band certifying model and sampling provenance.
* **Status**: **Fully operational (v0.1.0)** with a 27-test validation suite and automated rule-syncing scripts.

### 💀 [servo-skull](https://github.com/maurice-jobst/servo-skull)
A layout-preserving document ingestion engine:
* **Mechanism**: Extracts textual data from complex PDFs, HTML, and Office documents with layout preservation (integrating PyMuPDF and Microsoft MarkItDown), chunking text into an optimized FTS5 database grounding.
* **Status**: Deployed and active across workspace modules.

### 🏰 [homeserver-infra](https://github.com/maurice-jobst/homeserver-infra)
Ansible and Docker GitOps deployment configurations:
* **Mechanism**: Automates bare-metal system hardening, network partitioning, and isolated container stacks to host Ollama, SQLite FTS5 nodes, and private APIs.
* **Status**: Operational, orchestrating distributed system states.

### 🚃 [umo-pass-mtt](https://github.com/maurice-jobst/umo-pass-mtt) (CUBIC)
Integration models and strategical architectures for transit payment infrastructures:
* **Scope**: Technical specifications and payment schemas aligning with **Visa Contactless Transit (MTT)** and **Mastercard Transit Implementation Guidelines**.
* **Status**: Deployed in production scoping folders.

---

## ✙ Active Construction Tasks

- [x] **[Chant-Task-001]** Implement core three-tier compression pipeline and regex preservers.
- [x] **[Chant-Task-002]** Implement three-band SEAL validation and heresy detection.
- [x] **[Chant-Task-003]** Implement CLI and Scriptorum logging.
- [ ] **[Priest-Task-001]** Technical implementation of autonomous self-healing loops for local daemon processes.
- [ ] **[Dream-Task-001]** Implement sqlite-based consolidation heuristic running four-quadrant (Tzeentch/Slaanesh/Nurgle/Khorne) distillation.

---

## 🚀 Sovereign Infrastructure Deployment
### Prerequisites
* **Control Node**: macOS workstation (Apple Silicon) with SSH key access configured to `homeserver`.
* **Execution Node**: Intel NUC or Ubuntu bare-metal server.
* **Inference Substrate**: Ollama daemon hosting local quantized models.

### Reconcile Systems
```bash
# 1. Clone the core GitOps control plane
git clone https://github.com/maurice-jobst/homeserver-infra.git

# 2. Setup your local environment
cd homeserver-infra
uv venv && source .venv/bin/activate

# 3. Provision bare-metal node
ansible-playbook -i inventory.ini bootstrap.yml
```

---

<div align="center">

**Built with dedication | Powered by local hardware & Apple Silicon**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Maurice%20Jobst-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mauricejobst/)
[![GitHub](https://img.shields.io/badge/GitHub-maurice--jobst-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/maurice-jobst)
[![Email](https://img.shields.io/badge/Email-maurice.jobst%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:maurice.jobst@gmail.com)

*Last updated: May 2026 (Chant v0.1.0 Release)*

</div>
