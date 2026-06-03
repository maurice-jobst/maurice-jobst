# Maurice Jobst

**Senior Product & Delivery Lead · Local-First AI Architect · Human-Orchestration Systems**
*Frankfurt am Main · 15+ years of delivery across regulated fintech, mobility & public-sector*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Maurice%20Jobst-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mauricejobst/)
[![GitHub](https://img.shields.io/badge/GitHub-maurice--jobst-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/maurice-jobst)
[![Focus](https://img.shields.io/badge/Focus-Sovereign%20B2B%20%26%20B2G-2E7D32?style=flat-square)](#where-im-pointed)
[![AI](https://img.shields.io/badge/AI-Local--First%20·%20Air--Gapped-6A1B9A?style=flat-square)](#what-im-building-now)

---

## About me

I operate at the intersection of complex regulatory frameworks and advanced local-first technology. My journey began writing Turbo Pascal on an Atari ST and learning English from a Game Boy and *Dune II* — then organizing early multiplayer communities that became a consequence-free training ground for leading distributed, cross-functional teams long before "remote work" was a corporate standard. *(One of those games was Warhammer Online; I later worked at its European publisher, GOA Games — my name is in the credits somewhere, which still makes me grin.)*

For over 15 years I've translated ambitious business visions into resilient, high-throughput execution across highly regulated environments — PayPal, Avira, Tipico, Velvon, and Cubic — from cloud-native core banking under BaFin scrutiny to public-transport platforms serving millions. The role stays constant: stand between ambitious stakeholders and complicated systems and make them cooperate, transparently.

Today my engineering focus is **sovereign, local-first AI architecture**. I design air-gapped, GDPR-compliant agentic substrates on Apple Silicon — deterministic-first ingestion and execution that guarantees data integrity, privacy, and performance without fragile cloud-dependent APIs. Everything runs on Mac-as-Code principles (`chezmoi`, versioned manifests) and local GitOps, so the infrastructure and the local LLM runtimes alike are fully reproducible, auditable, and resilient.

I lead hybrid orchestration systems where human teams and local AI agents collaborate under strict engineering guidelines. The crew is just different now — these days I summon part of it, and right now that work honestly feels a little like being a cabbalist, a conjurer of constructs. That's only the current name for it; the constant is the threshold between business and technology, and I've stood there my whole life.

I'm based in Frankfurt am Main, the town I was born in, raising my daughter in a world that's AI-native from the start — and trying to be an AI-native dad worth having. *(My wife taught English once, in Brazil; now she's at Nintendo, building the machines that do the teaching.)* I build open, sovereign, secure systems made to stand up to regulatory and architectural scrutiny — honest work, out in the open.

---

## What I'm building now

Most "human-in-the-loop" AI treats the human as a brake on an autonomous agent. I'm working on the inversion: **the AI orchestrates the human.** It holds the situational picture and does the framing; the human keeps the authority and acts. There's real evidence behind this — Fügener et al. (*Information Systems Research*, 2022) found human–AI teams beat the AI alone *only when the AI delegated to the human*, because people systematically misjudge their own competence.

Applied to delivery and people-leadership, that becomes a system that runs a manager through a living, rule-anchored playbook — grounding every claim against a verifiable source, anchoring every decision to a citable rule, and surfacing exactly where a human left something implicit. Three principles keep it trustworthy:

- **Grounding over fluency** — deterministic ground truth first; the generative layer is fallible and always scored against the source.
- **Symmetric accountability** — the same machinery that audits a stakeholder audits the operator too, on identical terms.
- **Name dysfunction, don't launder it** — when the conditions for honest work are absent, the system says so instead of producing a tidy plan that pretends otherwise.

---

## Open-source work

> I name my tools so I remember them — the name carries the job. The Mechanicus flavor is deliberate: a dense, self-consistent vocabulary compresses well, makes rules behave like dogma a model follows reliably, and turns any out-of-canon term into a cheap tripwire for tampering. Where lore and engineering disagree, engineering wins. *(All 40k marks © Games Workshop; unofficial, non-commercial.)*

| Project | What it is |
|---|---|
| **[binaric-chant](https://github.com/maurice-jobst/binaric-chant)** | Three-tier prompt-compression library (~65% token reduction) with a cryptographic **SEAL** — SHA-256 integrity hash plus a canary that detects model substitution or tampering. *More mechanism than code.* |
| **[servo-skull](https://github.com/maurice-jobst/servo-skull)** | Layout-preserving document ingestion (PyMuPDF + MarkItDown) into a fast local FTS5 store. The deterministic front door — no model invents what a document said. |
| **[caveman_40k](https://github.com/maurice-jobst/caveman_40k)** | A prompt-compression skill that strips grammatical function words while keeping the semantic payload intact. The empirical precursor to the pipeline above. |
| **[c41-tcai-engine](https://github.com/maurice-jobst/c41-tcai-engine)** | Reference implementation of a deterministic synthesis engine: parses raw documents into structured domain codices with extraction and hallucination scoring. |

---

## Proprietary & client work *(described, not linked)*

The internal Git origin is the authority; this profile is the showcase. Private systems are described at the architecture level only.

- **Sovereign synthesis engine.** A deterministic-first pipeline that turns heterogeneous source documents into grounded, rule-anchored backlogs — and, increasingly, into a living playbook that orchestrates the human running the project. Demonstrated: a hand-written 36-story backlog reproduced as 29 fully rule-traceable stories at a **0.00 hallucination score**, catching errors the human-written original contained.
- **GitOps control plane.** Idempotent bare-metal hardening, network partitioning, isolated container stacks, `sops`+`age`-encrypted secrets *in-repo* (the key never leaves the control plane), and a sovereign private origin. If the substrate died tomorrow, it rebuilds from git to a known-good state.
- **Contactless transit-payment architecture** *(client-confidential)*. Open-loop fare-payment integration aligned with Visa Contactless Transit (MTT) and Mastercard Transit guidelines, delivered as a version-controlled feature backlog and technical specification set.

---

## The setup

A federated, two-node environment I control end-to-end, so private data stays on hardware I own and every AI output traces back to a deterministic ground truth.

- **Control plane** — Apple Silicon. Agentic orchestration, local LLM inference (Ollama), deterministic document synthesis. Reproducible via `chezmoi` + a versioned `Brewfile`.
- **Substrate** — bare-metal Ubuntu, deliberately disposable. Isolated container stacks, hardened host, private Git origin with FTS5 retrieval.
- **The doctrine** — code moves by GitOps, never by file-sync. The control plane is the truth; the substrate is reconstructable.

---

## Track record

- Led the turnaround of a flagship public-transport app from **1.6 to ~4.0 stars**, scaling to **3M+ users** through the politically critical *Deutschland-Ticket* launch with zero downtime — and secured **€2M+ in annual renewals** by aligning delivery to the client's fiscal reality.
- Delivered **audit-ready, regulator-grade** software for a cloud-native core banking system on GCP, mapping every component to its regulatory requirement (BaFin / KWG) to clear pre-license audits — proving a German banking core could run compliantly on a US hyperscaler.
- 15+ years across **fintech, public sector, cybersecurity, and mobility**. PRINCE2, PSPO, PSM I; Executive MBA. Bilingual in **German regulatory rigour** and **US/SaaS commercial agility**.

---

## Where I'm pointed

I'm most useful where **high stakes, heavy regulation, and powerful new technology meet** — and where someone has to make all three coexist honestly. I'm pointed at **public-sector / B2G and EU-institution leadership and principal/advisory roles** — Berlin, Brussels, Frankfurt — turning digital sovereignty, AI governance, and privacy-by-design from buzzwords into architecture that actually holds. The orchestrator who stands between leadership, regulation, and engineering and makes the three cooperate.

---

## Reach me

- **LinkedIn** — [linkedin.com/in/mauricejobst](https://www.linkedin.com/in/mauricejobst/) *(best place to start a conversation)*
- **GitHub** — [github.com/maurice-jobst](https://github.com/maurice-jobst)
- **Email** — maurice.jobst@gmail.com

*Built in Germany, on silicon I own. Honest work, out in the open.*

[![LinkedIn](https://img.shields.io/badge/Let's%20talk-on%20LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mauricejobst/)
