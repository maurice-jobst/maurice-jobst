# Running a personal infrastructure estate like a regulated hub-and-spoke organization

*A dozen-plus repositories, two physical sites, and domains that must never mix run on a single operating model. That model is what a regulated hub-and-spoke organization needs.*

I run a personal infrastructure estate for my household: a containerized home server, a managed workstation, a private git forge, a second physical site, and a dozen-plus active repositories spanning infrastructure, a small business, and personal administration. Three domains must never mix, across two sites, with one part-time operator, and AI sessions run in the loop across all of it every day.

That combination is unmanageable by memory and meetings. It runs anyway, because everything reduces to one shape.

## One reconcile shape, one direction

Every change moves the same way: **author on the workstation → commit to the canonical forge → converge onto the target**. Infrastructure converges via Ansible onto the hosts. Repo governance (labels, branch protection, milestones) converges via idempotent provisioning scripts onto the forge. Documents converge via protected-branch PR flow into their repos. Nothing is ever fixed *on* a target; the fix is encoded at the source, and the pipeline reapplies it. A hand-edit on a live host is a fork, not a shortcut, and every fork becomes drift later.

The payoff of one shape is transfer: an operator, human or AI, who has learned the shape once can act in any spoke (the small-business repo, the personal-documents archive, the infrastructure tree) because the mechanics of landing a change never change from one spoke to the next. The content changes; the mechanics don't.

## Hub and spoke: doctrine lives once

Cross-cutting doctrine (the git model, secrets handling, the AI operating rules) lives once, in the hub. Spokes carry a self-contained brief, budgeted to orient a cold session fast, that cites the hub rather than restating it. The alternative is a dozen drifting copies of the same paragraph, each one read by an AI session as equally authoritative. In an AI workforce, duplication is a correctness problem, not just a style problem.

The standard is enforced, not aspirational. A small dependency-free validator walks the federation register and reports green or red per repo: canonical file present, tool-specific files symlinked rather than diverged, the agent-facing surface conformant. Compliance with the doc standard is a mechanical check rather than something anyone has to remember.

## Time to dock a new unit

The measure of an operating model is what it costs to dock a new unit. In this federation, docking a spoke (new repo, governance, briefing doc, issue taxonomy, protected mainline) takes a converge script and a PR, not a project. In one recent session I restructured a personal-documents archive to current conventions, converged its forge governance (scoped labels, issue templates, branch protection) via an API script, enforced a privacy fence for a sensitive personal dataset in tool configuration rather than prose, and landed the whole change through the same protected PR flow the infrastructure uses. One session produced a reviewable, production-grade result.

That speed comes from deleting three usual costs. Each unit reuses one shape instead of a bespoke process. The hub already holds the doctrine, so there's no archaeology. And everything converges from code, so there's nothing to reconstruct later by hand.

## Where AI belongs, and where it doesn't

The doctrine is one sentence: **AI at the edges, deterministic core.** AI authors config, drafts documents, triages findings, and proposes plans. It never sits inside a path that must be byte-reproducible: converge, deploy, secrets. A deterministic sweep audits the estate weekly with pure reads and structured output, so it cannot hallucinate a green light. The AI reasons about the findings afterward.

Write access is governed the same way for both kinds of operator. The mainline is push-protected, everything lands as a reviewable PR, and review is symmetric: the human reviews the AI's work, and the AI reviews the human's. Where the model must not read at all, a category of sensitive personal records, the fence is a deny rule in the tool's permission layer rather than a sentence in a README.

## The generalizable part

This estate is household-scale by design, and I don't claim otherwise. The transferable asset is the operating model, not the headcount. But map the nouns and this becomes a regulated enterprise's problem statement: a cooperative banking group, a KRITIS operator, any hub-and-spoke organization has decentralized units that must dock onto central doctrine without a central bottleneck, regulators who ask "prove the estate matches its policy" rather than "do you have a policy," and AI capability that must be adopted without ever entering the audited core.

The federation answers are the enterprise answers, shrunk but not simplified. Doctrine lives once and gets cited rather than copied. Units dock through one reconcile shape, so onboarding cost collapses. A validator checks conformance instead of a committee. AI operates at the edges under symmetric review, and the irreversible paths stay deterministic. Drift, whether in config, docs, or policy, is the primary enemy at any scale, because it's always the same gap: what the organization believes about itself versus what is actually running.

If your operating model depends on people remembering the doctrine, it isn't a federation, it's folklore with an org chart. Make the doctrine a hub, the units spokes, the landing path one shape, and the check a machine. Then adding the next unit, or the next AI, takes a day like any other.
