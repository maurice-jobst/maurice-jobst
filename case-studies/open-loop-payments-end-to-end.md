# Open-loop payments, owned end to end

*Cubic Transportation Systems, 2026–present · Senior Product Manager, Frankfurt, global remit. Umo Pass: open-loop transit payments from EMV acceptance at the validator to the account-based back office, with European Payments Initiative (EPI) integration.*
*Client, vendor and commercial specifics are confidential. Everything below stays at architecture level, every fact is on my resume or in a named public source, and the fuller version is available in conversation.*

## The situation

Transit fare collection is moving from proprietary hardware and closed-loop cards to software: account-based ticketing, where the card in your pocket or the phone in your hand is the ticket, and the system decides afterwards what the journey cost. It is one of those rare market shifts where the winning architecture is already known (the open procurements say so), and the question is who builds it well.

My remit is the open-loop payments stack for the Umo platform, end to end: EMV acceptance at the validator, through authorisation and risk, to the account-based back office that aggregates taps into fares and settles them. Alongside it sits the European layer: integrating European Payments Initiative (EPI) digital identity, which is where transit acceptance meets European payment sovereignty. Negotiating with banks and payment service providers at technical and regulatory level, across the acceptance-to-settlement chain, is the day job.

## Why a gate is the hardest point-of-sale in payments

Walk through one declined tap, because every architectural decision in open-loop traces back to it.

**Latency first.** A station gate has to validate and open while the passenger is still walking. Transport for London specified 500 ms for that transaction, a figure published in Mastercard's own TfL case study. Miss that budget and you do not get a slow gate; you get a queue at rush hour and a gate somebody has to open for free. Card-based transit meets the budget by doing the cryptographic work offline at the reader: risk decided locally, settlement later, no round trip. That architecture exists because the latency budget forced it. A payment scheme built for e-commerce checkout starts from the opposite assumption: the customer has already stopped walking, and authorisation is online by construction. Putting such a scheme at a gate line is an architectural negotiation, not an integration task.

**Then the part that is a rulebook problem, not an engineering one.** Account-based ticketing opens the gate first and calculates the fare later, often aggregating a day of travel into a single charge. Somebody extends credit for the length of that window. On card rails, that risk sits inside decades of scheme rules: authorisation holds, liability shift, chargeback rights, a defined process for when it goes wrong. SEPA Instant is irrevocable by design. Excellent for a merchant, and it means the card playbook does not transfer. An operator carrying a day of aggregated fares needs to know who owns the loss when the account is empty at midnight. The primitives exist on paper: the European Payments Council's SPAA scheme defines Dynamic Recurring Payments and, more to the point, Payment Certainty Mechanisms, the industry's own name for this exact gap. Whether new European schemes adopt them, and what banks charge for them, is the question I put to the scheme side of the table.

## What owning it end to end means

- **One owner across the chain.** Acceptance at the device, the EMV and certification layer, authorisation and risk, fare aggregation, settlement, and the scheme relationships are one product remit, not five departmental slices. The failure mode of transit payments programs is that the gate team and the settlement team meet for the first time in an incident review.
- **The regulatory layer is part of the product.** PSD2 today, PSD3/PSR on a published timetable, scheme rulebooks, and the sovereignty agenda behind EPI are inputs to architecture decisions, not compliance paperwork appended to them. This is the same discipline I ran at a BaFin-supervised core-banking build: turn the obligation into a testable system property before an engineer has to guess.
- **The timezone is a handoff, not a tax.** Product direction sits with me in Frankfurt; engineering sits hours away. Run deliberately, the gap means work moves while the other side sleeps: a scheduling design problem, not a staffing complaint.

## What this case study cannot show you

Published outcome numbers: the remit is months old, and I do not manufacture percentages. The scope and the architecture are the claim here. The numbers live next door: the [Deutschland-Ticket turnaround](deutschland-ticket-turnaround.md) on the same platform carries 3M+ users, a 1.6 → 4.0 app-store rating, and €2M+ in annual renewals.

## Why this seat matters

Every other engagement on my resume is delivery under regulatory or political constraint. This one is architecture on the winning side of a market shift: account-based, open-loop, software-defined fare collection is what transit authorities worldwide are procuring, and I am building it inside the industry that has to make the transition. Combined with the European layer (EPI, the digital euro pilot, PSD3/PSR arriving on a published timetable), it is the vantage point the payments market prices fastest, and it is where my payments thread (PayPal, gaming-payments compliance, multi-gateway platforms, BaFin-supervised core banking) was always heading.

---

*Related: [turning a banking act into engineering specifications](banking-act-to-specifications.md) shows the regulatory-translation method; [the Deutschland-Ticket turnaround](deutschland-ticket-turnaround.md) shows the delivery record on the same platform.*
