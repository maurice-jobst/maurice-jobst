# AGENTS.md — Profile (maurice-jobst)

The GitHub profile shop-window for **Maurice Jobst** (`github.com/maurice-jobst`) · Federation role: **public-facing showcase spoke** · Sync-zone: local git (public origin).
Self-contained for ≤50k-token context. The deliverable is `README.md` itself — the profile that renders on the GitHub profile page.
Federation source of truth: the hub's `AGENTS.md` (`~/1_Projects/AGENTS.md`) — cite it, don't copy it.
> CLAUDE.md is a symlink to this file. No GEMINI.md (Gemini does not run here).

**What this workspace is.** A public git repo whose `README.md` is rendered as the GitHub profile landing page. Curated shop-window for B2B/B2G work — open-source projects link out, proprietary ones are described at the architecture level only.

## §0 Non-negotiable invariants
1. **Public-facing — no internal or PII content.** Everything here is world-readable. Never commit private paths, secrets, NUC IPs, client names, pricing, or stakeholder detail. Client engagements stay architecture-level and explicitly marked confidential.
2. **Confidential repos stay described, not linked.** Private/proprietary systems (control plane, client work) get prose walkthroughs only — no links to private origins, no leaking internal repo structure.
3. **Cite, don't duplicate.** Federation facts live in the hub; do not restate internal doctrine here.

## §1 Repo map
- `README.md` — the rendered profile (the single deliverable). Badges, systems narrative, open-source project links, "available on request" notes for private work.

## §3 Decision rules
- *Adding a project to the profile?* → public + open-source → link the GitHub repo. Private/client → architecture-level prose only, mark confidential, no link.
- *Editing the profile?* → edit `README.md`, keep badges current, commit. Do not push unless explicitly asked.

## Voice & doctrine
Polished, confident, B2B/B2G-audience. "Sovereign engineering / local-first AI" framing. WH40k/Mechanicus flavor is intentional shop-window styling. Full federation doctrine on-demand in the hub.
