# Turning a banking act into engineering specifications

*Velvon Bank, 2019–2020 · Product Manager, Munich. Core banking on Google Cloud Platform, under BaFin scrutiny, for a German banking-license acquisition.*
*Client and deal specifics are confidential. Everything below stays at architecture level, every fact is on my resume, and the fuller version is available in conversation.*

## The situation

A startup was acquiring a German banking license. That means building core banking infrastructure that the Bundesanstalt für Finanzdienstleistungsaufsicht will examine, on a cloud platform, at a pace set by the deal rather than by the engineering.

Two clocks ran against each other. The delivery clock wanted weekly releases and a team that could change its mind. The supervisory clock wanted a system whose behaviour you could describe in advance, evidence after the fact, and defend to an examiner who had never met the team.

## Why a legal text is not a specification

The Kreditwesengesetz tells you what a credit institution must be true of. It does not tell an engineer what to build. Between the two sits the work almost nobody staffs properly, and it is the work that decides whether the audit goes well.

Take one requirement. The law wants client funds separated from the institution's own. An engineer reading that sentence has questions the sentence does not answer. Separated at which layer, the ledger or the account? A transfer landing mid-reconciliation goes where? Which failure modes must be impossible rather than unlikely, and which of those does the platform underneath you guarantee?

Leave those open and each engineer resolves them differently. Six months later the system works, nobody can say precisely how, and the examiner asks the one question that was never decided.

## What I did

- **Translated KWG requirements into deterministic engineering specifications.** Each obligation became a stated system property with its own acceptance criteria, written so a developer could build against it and an auditor could test it. Same sentence, both readers.
- **Mapped ledger and transaction-isolation boundaries** for the core banking infrastructure on GCP. Where the cloud platform's own guarantees stopped, the specification said so and named what the application had to do instead. Assumed guarantees are how regulated cloud programs fail their first audit.
- **Held the line between startup speed and supervisory expectation** rather than picking a side. The team kept its release cadence. The properties that carried regulatory weight moved to a slower, evidenced track with a named owner.

## The method

Three rules, and they have survived every regulated program I have run since.

**Turn every obligation into a testable property.** "Client funds are segregated" is a claim. "No settlement path can move client funds into an own-account ledger, enforced at the ledger boundary and covered by test X" is a property. Auditors accept properties. They argue with claims.

**Decide the ambiguity in writing, once.** Every legal text has gaps that engineers must fill. Fill them yourself, in the specification, with the reasoning attached. Otherwise the gap is filled anyway, silently, differently, by whoever hits it first at 17:00 on a Friday.

**Name the boundary where your platform's guarantees end.** Regulated cloud work lives or dies on this. Write down what the provider guarantees, what it does not, and what your application does about the difference.

## What this case study cannot show you

No star rating, no renewal figure. The [Deutschland-Ticket turnaround](deutschland-ticket-turnaround.md) alongside this one carries the numbers. This engagement carries the method, and the method is the part that transfers.

## Why it matters again now

Payments is the deepest thread in my fifteen years: PayPal in Dublin, payment-gateway and gaming-license compliance at Tipico, multi-gateway integration under sub-second latency and failover requirements at Oddspedia, BaFin-supervised core banking here, and today European payment sovereignty at Cubic, integrating European Payments Initiative digital identity with account-centric transit fare payment.

The same translation problem is arriving again, at scale, on a published timetable. PSD3 and the Payment Services Regulation reached final compromise texts in April 2026, with application expected around 2028 and the Verification of Payee extension roughly six months behind it. Verification of Payee has been mandatory for euro instant credit transfers since October 2025. The digital euro pilot phase begins staffing now. Every payment service provider in the EU is about to turn several hundred pages of regulation into systems that examiners will test.

That is the same job as the one above, with more zeroes. It is the job I want.

---

*Related: [running an infrastructure estate like a regulated hub-and-spoke organization](hub-and-spoke-estate.md) applies the same doctrine to an operating model instead of a ledger.*
