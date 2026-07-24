# Running a personal infrastructure estate like a regulated hub-and-spoke organization

*A dozen-plus repositories, two physical sites and three domains that must never mix, run by one part-time operator on a single operating model. That model is what a regulated hub-and-spoke organization needs.*

I run a personal infrastructure estate for my household: a containerized home server, a managed workstation, a private git forge, a second physical site, and a dozen-plus active repositories spanning infrastructure, a small business and personal administration. Three domains must never mix, across two sites, with one part-time operator, and AI sessions run in the loop across all of it every day.

You cannot hold that in your head, and meetings will not save you. It runs anyway, because every change reduces to one shape.

## One reconcile shape, one direction

Every change moves the same way: **author on the workstation → commit to the canonical forge → converge onto the target**. Infrastructure converges via Ansible onto the hosts. Repo governance (labels, branch protection, milestones) converges via idempotent provisioning scripts onto the forge. Documents converge via protected-branch PR flow into their repos.

I never fix anything *on* a target. I encode the fix at the source and let the pipeline reapply it. Hand-edit a live host and you have forked it, and that fork comes back later as drift.

One shape buys transfer. An operator who has learned it once, human or AI, can act in any spoke (the small-business repo, the personal-documents archive, the infrastructure tree), because landing a change works identically everywhere. Only the content differs.

## Hub and spoke: doctrine lives once

Cross-cutting doctrine (the git model, secrets handling, the AI operating rules) lives once, in the hub. Each spoke carries a short self-contained brief that cites the hub instead of restating it, budgeted to orient a cold session fast. Restate it and you get a dozen drifting copies of the same paragraph, each one read by an AI session as equally authoritative. Duplication turns into a correctness problem the moment your workforce includes agents.

A small dependency-free validator walks the federation register and reports green or red per repo: canonical file present, tool-specific files symlinked instead of diverged, agent-facing surface conformant. Nobody has to remember the doc standard, because the machine checks it.

## Time to dock a new unit

Judge an operating model by what it costs to dock a new unit. Here, docking a spoke (new repo, governance, briefing doc, issue taxonomy, protected mainline) takes a converge script and a PR.

In one recent session I restructured a personal-documents archive to current conventions, converged its forge governance (scoped labels, issue templates, branch protection) through an API script, fenced a sensitive personal dataset in tool configuration rather than in prose, and landed the whole change through the same protected PR flow the infrastructure uses.

That speed comes from three costs I deleted. Each unit reuses one shape instead of a bespoke process. The hub already holds the doctrine, so nobody does archaeology. Everything converges from code, so I never reconstruct state by hand.

## Where AI belongs, and where it does not

The doctrine fits in one sentence: **AI at the edges, deterministic core.** The agent authors config, drafts documents, triages findings and proposes plans. It never sits inside a path that must be byte-reproducible: converge, deploy, secrets. A deterministic sweep audits the estate weekly with pure reads and structured output, so it cannot hallucinate a green light. The agent reasons about the findings afterward.

Both kinds of operator get the same write rules. The mainline is push-protected, every change lands as a reviewable PR, and review runs in both directions: I review the agent's work, and the agent reviews mine. One category of sensitive personal records the model must never read at all, and that fence is a deny rule in the tool's permission layer instead of a sentence in a README.

## The generalizable part

This estate is household-scale by design, and I do not claim otherwise. What transfers is the operating model.

Map the nouns and you get a regulated enterprise's problem statement. A cooperative banking group or a KRITIS operator has decentralized units that must dock onto central doctrine without a central bottleneck, regulators who ask them to *prove the estate matches its policy* rather than to produce one, and AI capability to adopt without ever letting it into the audited core.

The federation answers are the enterprise answers at a smaller scale:

| Problem | Answer |
|---|---|
| Doctrine drifts across units | It lives once in the hub and gets cited, never copied |
| Onboarding a unit costs a project | Every unit docks through one reconcile shape |
| Conformance depends on a committee | A validator checks it per repo, green or red |
| AI capability threatens the audited core | AI at the edges under symmetric review, irreversible paths deterministic |

Drift is the primary enemy at any scale, in config, in docs or in policy, because it is always the same gap: what the organization believes about itself versus what is actually running.

An operating model that depends on people remembering the doctrine will drift. Put the doctrine in a hub, dock the units through one landing path, and let a machine do the checking. Then the next unit, or the next agent, costs you a day.
