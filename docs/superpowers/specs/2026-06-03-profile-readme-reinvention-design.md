# Design — GitHub Profile README Reinvention

**Date:** 2026-06-03
**Deliverable:** `README.md` in `maurice-jobst/maurice-jobst` (the rendered GitHub profile landing page)
**Status:** Draft for review

---

## 1 · Goal

Reinvent the GitHub profile so it reads, first, as an **honest and open** professional
shop-window that complements LinkedIn — and second, carries a light, self-aware
**mythological framing** (the AI summoner / Cabbalist) as connective ambience, never as
costume.

The previous live README leaned heavy on Adeptus Mechanicus styling (typing SVG, ASCII
forge, trophy wall, "Grand Master of the Librarium"). This reinvention deliberately dials
that **down** and re-centres the page on a human story.

## 2 · Audience, strategy & voice

- **Primary audience:** recruiters, founders, family offices, and **public-sector / B2G
  decision-makers in Berlin, Brussels, and Frankfurt** who arrive from LinkedIn or a cold
  search. Must read clean and credible to someone who knows nothing about DAoC or 40k.
- **Secondary audience:** peers and fellow builders who recognise the references.
- **Strategic intent (stated, not published):** this profile is a **showcase only** — the
  internal Gitea is the authority and holds nothing private/secret reaches GitHub. Its job
  is to *put Maurice on the radar* for **high-level B2G leadership / advisory roles** — the
  person who has personally built this for two decades and is therefore most useful now in a
  leadership seat: an orchestrator who holds the picture and acts with delegated authority,
  standing between leadership, regulation, and engineering and making the three cooperate.
  *(The deeper motive — financial freedom to fund his own research — stays off the page.)*
- **Voice:** warm, honest, plain-spoken, first-person. Professional substance leads every
  section. Mythology is *seasoning* — a knowing aside, never a lore wall.
- **The dial (agreed):** "I want people to see I am honest and open without exposing too
  much of the nerdiness." Human-and-honest first; the universe is a wink.

### 2026 best-practice constraints (from current GitHub-profile guidance)

- **Signal, not noise.** No badge walls, no resume-dump, no "expert in 47 technologies."
  Clean and scannable.
- **Lead with who/what** (1–2 lines) → current threads (2–3) → featured repos (3–5, one
  line each) → how to reach me (2–3 links). Mirror this shape.
- **Senior-leader-with-private-work pattern:** describe large-scale systems at the
  architecture level — responsibilities, scaling milestones, leadership footprint — without
  exposing code. This fits Maurice exactly (Gitea is the authority).
- **Featured/pinned repos carry weight:** ensure the showcase repos are pin-worthy and each
  has a one-paragraph "what & why" README of its own (out of scope here, but note it).

## 3 · The framing doctrine

- **Operator = the summoner.** Maurice is the one who conjures and orchestrates.
- **Constructs = the 40k-named tools.** `servo-skull`, `binaric-chant`, etc. keep their
  names because they are real, shipped repos — the names live in the showcase section where
  they are justified, not stacked into the prose.
- **The persona is explicitly impermanent.** The about-me names the current lens
  (cabbalist / technomancer / conjurer) and openly says *it will change again*. The
  constant is the threshold between business and technology, not the costume.
- **No alias in the hero.** "Sandrox Peracutus / Cabbalist" does **not** appear in the
  customer-facing title block (per decision). The mythology surfaces only inside the
  About-me prose and the one-line repo-naming wink.

## 4 · The narrative spine (About-me)

The heart of the page. Not "I played raids" — the deeper, truer frame:

> A life spent at the threshold between business and technology, witnessing — and
> helping — technology rewrite how humans interact.

Beats, in order, kept light and evocative (not a spec-dump list):

1. **Lifelong threshold-dweller.** I've always stood where business meets technology.
2. **Tech as teacher & connector.** Analog phones becoming numpads; a Game Boy that taught
   me English; an Atari ST and my first lines of Turbo Pascal; a 486 from IBM; Dune II, my
   first RTS, teaching me English again. Technology as something that taught and connected,
   not just computed.
3. **Multiplayer as a leadership school.** Games gave me a free, consequence-free place to
   learn to lead people — coordinating strangers, building communities, leading distributed
   teams remotely before "remote work" was something anyone bragged about.
4. **The career.** That became the job: PayPal, Tipico, Avira, Velvon, Oddspedia, GOA Games
   (the European publisher of the worlds I'd been playing — my name is in the Warhammer
   credits somewhere, which still makes me grin), Cubic. Across Malta, Ireland, the UK,
   Switzerland, Los Angeles, and the Bodensee. Always the same role: stand between
   ambitious people and complicated systems and make the two cooperate, honestly.
5. **Now.** I'm still at that threshold. Right now it happens to feel like being a
   cabbalist — a conjurer summoning AI constructs to do the work a team used to, learning
   that once you have a dozen of them a few must manage the rest so you can keep your
   attention on the bigger picture. That's just the current name for it. It'll change again.
6. **Home.** Back in Frankfurt am Main, the town I was born in, raising my daughter in a
   world that's AI-native from the start — trying to be an AI-native dad worth having.

**Family thread (rhymes with the games→English motif):** games taught me English; the woman
I married taught English too — once in Brazil — and now works at Nintendo, building the
machines that do the teaching. Warm, human, on-theme.

> ✅ **Public-exposure decision (approved 2026-06-03).** Maurice approved: naming
> **Nintendo** as his wife's employer (deemed anonymous enough), and referencing **"my
> wife"** and **"my daughter"** — both **without names**. No further family-identifying
> detail beyond this.

## 5 · Section structure (`README.md`)

| # | Section | Intent | Persona level |
|---|---------|--------|---------------|
| 1 | **Hero / title block** | Real name, professional subtitle (*Senior Product & Delivery Lead · Local-First AI · Human-Orchestration Systems*), Frankfurt + 15+ yrs line, restrained badges (LinkedIn, GitHub, focus). No trophy wall; at most one quiet line. | None (fully professional) |
| 2 | **About me** | The threshold-life narrative from §4. The human heart of the page. | Light wink (cabbalist named as the current, impermanent lens) |
| 3 | **What I'm building now** | The thesis: LLM-as-human-orchestrator — the AI holds the picture and treats the human as one more interface in the loop. Local-first, Mac-as-code, Apple Silicon, privacy, paradigm-inversion. No over-claiming. | Minimal |
| 4 | **Open-source work** | Repo showcase. One-line intro earns the names: *"I name my tools so I remember them — the name carries the job."* Then `servo-skull`, `binaric-chant`, `caveman_40k` with what each actually does. | The 40k names live here (justified) |
| 5 | **The setup** | Brief: two-node sovereign, local-first, GitOps, Mac-as-code. Compact nod — NOT the heavy live ASCII forge. | Minimal |
| 6 | **Track record** | Evidence, persona-free: RMVgo 1.6→4.0 / 3M+ users / Deutschland-Ticket / €2M renewals; Velvon banking-license; 15+ yrs regulated sectors; certs (PRINCE2, PSPO, PSM, Exec MBA). | None |
| 7 | **Where I'm pointed** | Short, forward-looking positioning: most useful at the intersection of high stakes, heavy regulation, and new technology — public-sector / B2G & EU-institution leadership and principal/advisory roles (Berlin · Brussels · Frankfurt). The orchestrator who makes leadership, regulation, and engineering cooperate. No "seeking work" desperation; quiet confidence. | None |
| 8 | **Reach me / footer** | One closing line in-voice + a clean 2–3 link contact block: **LinkedIn (primary), GitHub, email**. LinkedIn is the conversion target — it must be prominent here AND as a hero badge. | Light |

**LinkedIn weaving (explicit):** `https://www.linkedin.com/in/mauricejobst/` appears (a) as a
badge in the hero block, and (b) as the first, most prominent link in the reach-me/footer
block. The page is a showcase whose call-to-action is "continue the conversation on
LinkedIn."

## 6 · Facts to use (grounded)

Career (from LinkedIn export + MauriceJobstProfile.md + user):
- **GOA Games** — European publisher of Dark Age of Camelot & Warhammer Online; early
  technical team leadership (origin chapter; exact dates to be confirmed by Maurice — name
  it date-light).
- **PayPal**, Dublin (2007–2010) — Business Analyst / PO internal tools; built automation.
- **Tipico**, Malta (2010–2012) — Customer Solutions Architect; payments/integration.
- **Avira** (2012–2014) — Product Owner; agile transformation, CRM/marketing automation.
- **Oddspedia / Tipico ecosystem** (2018–2019) — Head of Product Management.
- **Velvon Bank** (2019–2020) — Product Manager; cloud-native core banking on GCP; German
  banking-license acquisition; BaFin / KWG.
- **Cubic Transportation Systems** (2021–present) — Senior Product PM; RMVgo turnaround
  1.6→4.0 stars, 3M+ users, Deutschland-Ticket, €2M+ annual renewals, ~€4.5M portfolio.
- Education: Executive MBA, Dublin Business School. Certs: PRINCE2, PSPO, PSM I.
- Locations lived: Malta, Ireland, UK, Germany, Switzerland, Los Angeles, Bodensee. Now
  Frankfurt am Main (birthplace).

Open-source repos (public, linkable):
- **binaric-chant** — prompt-compression library (~65% token reduction) with a crypto SEAL
  (SHA-256 integrity + model-substitution canary).
- **servo-skull** — layout-preserving document ingestion (PyMuPDF + MarkItDown) into a fast
  local FTS5 store; deterministic front door.
- **caveman_40k** — prompt-compression skill; empirical precursor to the pipeline.

## 7 · Guardrails (profile repo AGENTS.md §0)

- **Public-facing — no PII beyond what Maurice explicitly approves.** No private paths, no
  secrets, no NUC IPs, no client names, no pricing, no stakeholder detail.
- **Client work stays architecture-level and confidential.** The Cubic transit / Visa-MTT
  work is described only at the level already public on LinkedIn (RMVgo, Deutschland-Ticket);
  no confidential MTT/Visa specifics, no internal codenames (no C⁴¹·⁵, Praxis, Cogitator,
  homeserver, Gitea, NUC).
- **Confidential/proprietary systems: described, not linked.** No links to private origins.
- **Honesty over flex.** No invented metrics, no over-claiming the AI thesis. Keep the
  existing GW-copyright / unofficial-fan-use disclaimer for the 40k names.
- **Do not push** to origin unless Maurice explicitly asks (AGENTS.md §3).

## 8 · Sample prose (the agreed dial)

```markdown
# Maurice Jobst
**Senior Product & Delivery Lead · Local-First AI · Human-Orchestration Systems**
*Frankfurt am Main · 15+ years of delivery across regulated fintech, mobility & public-sector*

## About me

I've spent my life at the threshold between business and technology — and I've watched
technology quietly rewrite how humans talk to each other the whole way through. I learned
English from a Game Boy and from Dune II before I learned it in a classroom. I wrote my
first lines of Turbo Pascal on an Atari ST, on a 486 that felt like a spaceship. Multiplayer
games turned out to be a free, consequence-free school for leading people: coordinating
strangers, building communities, running distributed teams remotely years before anyone
called it "remote work."

That became the job. PayPal, Tipico, Avira, Velvon, Oddspedia, Cubic — and, early on, GOA
Games, the European publisher of the very worlds I'd been playing. *(My name is in the
Warhammer credits somewhere, which still makes me grin.)* Malta, Ireland, the UK,
Switzerland, Los Angeles, the Bodensee — same role every time: stand between ambitious
people and complicated systems and make the two cooperate, honestly.

Only the crew is different now. These days I summon it — I build and orchestrate AI agents
to do the work a team used to, and I've learned the summoner's real lesson: once you've got
a dozen of them, a few have to manage the rest, so you can keep your attention on the bigger
picture. Right now that role feels like being a cabbalist, a conjurer. That's just the
current name for it — it'll change again. The threshold is the constant.

I'm back in Frankfurt am Main now, the town I was born in, raising my daughter in a world
that's AI-native from the start — and trying to be an AI-native dad worth having. Honest
work, out in the open, is the whole point of this page.
```

## 9 · Build approach

Single content artifact. After this spec is approved: write `README.md` in one pass,
preview the rendered markdown, iterate on tone with Maurice, commit (do **not** push).
Mirror to Gitea only if asked.
