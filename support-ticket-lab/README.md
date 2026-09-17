# support-ticket-service

Internal IT support ticket routing service for AcmeCorp.

Classifies inbound support requests from plain-English descriptions and routes them to
the correct team with a priority level and SLA commitment. Used by the Level-1 Help Desk
to reduce manual triage time.

---

## Background

The Help Desk team was spending ~35% of their time re-routing tickets that had been
assigned to the wrong queue. This service was written to automate the initial classification
step. It runs as a standalone Python module and can be called from any internal tool,
Slack bot, or portal that can execute a Python function.

The classification logic is keyword-based and covers the six most common issue categories
we see in the queue. Routing rules (team assignment, priority, SLA) are maintained in
`ticket_classifier.py` directly — no external config file or database required.

---

## Repository Structure

```
support-ticket-lab/
├── ticket_classifier.py        # Core classification and routing logic
├── requirements.txt            # Python dependencies
├── orchestrate_agent.yaml      # Agent definition for watsonx Orchestrate integration
├── sample_tickets/
│   ├── security_incident.json  # Example: phishing / credential compromise
│   ├── service_outage.json     # Example: portal down, HTTP 503
│   └── billing_escalation.json # Example: invoice dispute over $5,000
└── README.md                   # This file
```

---

## Requirements

- Python 3.11 or higher
- pip

Install dependencies:

```bash
pip install -r requirements.txt
```

Dependencies (`requirements.txt`):

| Package   | Version  | Purpose                              |
|-----------|----------|--------------------------------------|
| fastapi   | >=0.110  | REST API framework (for HTTP wrapper)|
| uvicorn   | >=0.29   | ASGI server                          |
| pydantic  | >=2.0    | Input/output data validation         |

> **Note:** `pydantic` and the standard library (`re`, `hashlib`) are all that
> `ticket_classifier.py` itself needs. `fastapi` and `uvicorn` are only required
> if you are running the HTTP wrapper.

---

## Running the Classifier Directly

The classifier can be run as a standalone script to verify routing logic against
the five built-in test cases:

```bash
python ticket_classifier.py
```

Expected output (abbreviated):

```
🔴 [CRITICAL] Security Incident — TKT-XXXXX
  Assigned to: Security Operations Center (SOC) | SLA: 1h | Confidence: 96%

🟠 [HIGH] Service Outage — TKT-XXXXX
  Assigned to: Site Reliability Engineering (SRE) | SLA: 4h | Confidence: 97%

🟠 [HIGH] Access & Permissions — TKT-XXXXX
  Assigned to: Identity & Access Management | SLA: 4h | Confidence: 94%

🟡 [MEDIUM] Billing Inquiry — TKT-XXXXX
  Assigned to: Finance — Senior Billing Specialist | SLA: 4h | Confidence: 93%

🟠 [HIGH] Performance Issue — TKT-XXXXX
  Assigned to: Platform Engineering | SLA: 8h | Confidence: 91%
```

---

## Classification Logic

The service works in four steps:

1. **Classify** — The ticket description is lowercased and matched against keyword
   lists in `CLASSIFICATION_RULES`. The first matching rule wins. If nothing matches,
   the ticket falls through to `General Support`.

2. **Extract** — Regex patterns pull out structured details from the description:
   dollar amounts, affected system names (portal, API, SSO, VPN, etc.), and
   error codes (e.g. `503`, `AUTH-401`).

3. **Route** — `ROUTING_RULES` maps each ticket type to a team, priority level
   (`CRITICAL / HIGH / MEDIUM / LOW`), and SLA in hours. There is one escalation rule:
   a Billing Inquiry with a mentioned dollar amount over $5,000 is automatically
   upgraded to HIGH priority and routed to a Senior Billing Specialist.

4. **Format** — A deterministic ticket ID (`TKT-NNNNN`) is generated from an MD5
   hash of the description + timestamp, and the result is returned as a `TicketResult`
   Pydantic model.

---

## Ticket Types and Routing

| Ticket Type          | Trigger Keywords (sample)                        | Priority | Team                              | SLA   |
|----------------------|--------------------------------------------------|----------|-----------------------------------|-------|
| Security Incident    | breach, phishing, malware, unauthorized          | CRITICAL | Security Operations Center (SOC)  | 1h    |
| Service Outage       | down, outage, 503, offline, unavailable          | HIGH     | Site Reliability Engineering (SRE)| 4h    |
| Performance Issue    | slow, timeout, latency, unresponsive             | HIGH     | Platform Engineering              | 8h    |
| Access & Permissions | locked out, password, SSO, MFA, can't log in     | HIGH     | Identity & Access Management      | 4h    |
| Billing Inquiry      | invoice, charge, refund, overcharge              | MEDIUM   | Finance — Billing Support         | 24h   |
| Billing (> $5,000)   | _(same as above, amount extracted > $5,000)_     | HIGH     | Finance — Senior Billing Specialist| 4h   |
| Feature Request      | feature, enhancement, suggestion, would like     | LOW      | Product Management                | 72h   |
| General Support      | _(no keyword match)_                             | MEDIUM   | Tier-1 Help Desk                  | 24h   |

---

## Using the Classifier in Your Code

```python
from ticket_classifier import classify_ticket, TicketRequest

result = classify_ticket(TicketRequest(
    description="The customer portal is completely offline. Error 503. All users locked out.",
    submitted_by="DevOps Team"
))

print(result.ticket_type)    # "Service Outage"
print(result.priority)       # "HIGH"
print(result.assigned_team)  # "Site Reliability Engineering (SRE)"
print(result.sla_hours)      # 4
print(result.ticket_id)      # "TKT-47823"
```

---

## Updating Classification Rules

All rules are defined as plain Python dictionaries at the top of `ticket_classifier.py`.
No database migration or config reload is required — edit and redeploy.

To add a new ticket type:

1. Add an entry to `CLASSIFICATION_RULES` with a `type`, `keywords` list, and `confidence` score.
2. Add a corresponding entry to `ROUTING_RULES` with `priority`, `team`, and `sla_hours`.
3. Run `python ticket_classifier.py` locally to verify the new type routes correctly.

---

## Known Limitations

- Classification is keyword-based and case-insensitive. Synonyms or unusual phrasing
  may fall through to `General Support` even if the intent is clear.
- The first matching rule wins — ticket descriptions that span multiple categories
  (e.g. a security incident that also causes an outage) will only be classified as
  the first match in `CLASSIFICATION_RULES`.
- There is no persistence layer. Ticket IDs are deterministic hashes and are not
  stored anywhere by this service.

---

## Maintainers

AcmeCorp IT Platform Team — `it-platform@acmecorp.internal`

Last updated: Q2 2025
