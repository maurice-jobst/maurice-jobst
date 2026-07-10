# Running a personal infrastructure estate like a regulated hub-and-spoke organization

*How a dozen-plus repositories, two physical sites, and domains that must never mix run on a single operating model — and why that model is exactly what a regulated hub-and-spoke organization needs.*

I run a personal infrastructure estate for my household: a containerized home server, a managed workstation, a private git forge, a second physical site, and a dozen-plus active repositories spanning infrastructure, a small business, and personal administration. Three domains that must never mix, two sites, one part-time operator — and AI sessions in the loop across all of it, every day.

That combination is unmanageable by memory and meetings. It runs anyway, because everything reduces to one shape.

## One reconcile shape, one direction

Every change moves the same way: **author on the workstation → commit to the canonical forge → converge onto the target**. Infrastructure converges via Ansible onto the hosts. Repo governance — labels, branch protection, milestones — converges via idempotent provisioning scripts onto the forge. Documents converge via protected-branch PR flow into their repos. Nothing is ever fixed *on* a target; the fix is encoded at the source and the pipeline reapplies it. A hand-edit on a live host isn't a shortcut, it's a fork — and every fork is future drift with a delay fuse.

The payoff of one shape isn't elegance, it's *transfer*: an operator (human or AI) who has learned the shape once can act in any spoke — the small-business repo, the personal-documents archive, the infrastructure tree — because the mechanics of "how does a change land here" never change. Only the content does.

## Hub and spoke: doctrine lives once

Cross-cutting doctrine — the git model, secrets handling, the AI operating rules — lives once, in the hub. Spokes carry a self-contained brief, budgeted to orient a cold session fast, that *cites* the hub rather than restating it. The alternative is a dozen drifting copies of the same paragraph, each read by an AI session as equally authoritative — in an AI workforce, duplication isn't a style problem, it's a correctness problem.

And the standard is enforced, not aspirational: a small dependency-free validator walks the federation register and reports green/red per repo — canonical file present, tool-specific files are symlinks not divergent copies, the agent-facing surface conformant. Compliance with the doc standard is a mechanical check, not a memory.

## Radical time-to-production

The measure of an operating model is what it costs to dock a new unit. In this federation, docking a spoke — new repo, governance, briefing doc, issue taxonomy, protected mainline — is a converge script and a PR, not a project. In one recent session: a personal-documents archive was restructured to current conventions, its forge governance (scoped labels, issue templates, branch protection) converged via API script, a privacy fence for a sensitive personal dataset enforced in tool configuration rather than prose, and the whole change landed through the same protected PR flow the infrastructure uses. One session, production-grade, reviewable.

That speed isn't heroics. It's what's left when the three usual costs are deleted: no bespoke process per unit (one shape), no doctrine archaeology (the hub has it), no click-ops to reconstruct later (everything converges from code).

## Where AI belongs — and where it must not

The doctrine is one sentence: **AI at the edges, deterministic core.** AI authors config, drafts documents, triages findings, proposes plans. It never sits inside a path that must be byte-reproducible — converge, deploy, secrets. A deterministic sweep audits the estate weekly with pure reads and structured output, precisely so it *cannot* hallucinate a green light; the AI reasons about its findings afterwards.

Write access is governed the same way for both species of operator: the mainline is push-protected, everything lands as a reviewable PR, and review is symmetric — the human reviews the AI's work, the AI reviews the human's. Where the model must not read at all (a category of sensitive personal records), the fence is a deny rule in the tool's permission layer, not a polite sentence in a README — 2026 taught everyone the difference.

## The generalizable part

This estate is household-scale by design, and I make no claim it isn't: the transferable asset is the operating model, not the headcount. But map the nouns and this is a regulated enterprise's problem statement. A cooperative banking group, a KRITIS operator, any hub-and-spoke organization: decentralized units that must dock onto central doctrine without a central bottleneck; regulators who ask not "do you have a policy" but "prove the estate matches it"; AI capability that must be adopted without ever entering the audited core.

The federation answers are the enterprise answers, shrunk but not simplified: doctrine lives once and is cited, not copied. Units dock through one reconcile shape, so onboarding cost collapses. Conformance is a validator, not a committee. AI operates at the edges under symmetric review, and the irreversible paths stay deterministic. Drift — config drift, doc drift, policy drift — is treated as the primary enemy, because at any scale it is the same thing: the gap between what the organization believes about itself and what is actually running.

If your operating model depends on people remembering the doctrine, you don't have a federation — you have a folklore with an org chart. Make the doctrine a hub, the units spokes, the landing path one shape, and the check a machine. Then adding the next unit — or the next AI — is Tuesday.
