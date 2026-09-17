"""
Ticket Classifier — IBM TechXchange Partner Lab
================================================
A standalone Python module that classifies and routes IT support tickets
from plain-English descriptions.

This file is the STARTING POINT for the lab.
Participants use Bob to understand it, then wrap it in a FastAPI endpoint,
then deploy that endpoint to IBM Code Engine.

No external APIs. No environment variables. Runs locally with zero setup.

Classification logic:
  1. Classify the issue type from keywords
  2. Extract structured details (amounts, systems, error codes)
  3. Apply routing rules to determine team, priority, and SLA
  4. Return a structured TicketResult

Extension ideas (build-on-your-own after the lab):
  - Replace keyword classification with IBM watsonx.ai Granite model
  - After classification, POST to ServiceNow / Jira to create a real ticket
  - POST to Slack / Teams to notify the assigned team immediately
  - Register as a tool in watsonx Orchestrate so an agent calls this endpoint
"""

from pydantic import BaseModel, Field
from typing import Optional
import re
import hashlib
import time


# ── Data models ───────────────────────────────────────────────────────────────

class TicketRequest(BaseModel):
    """Input: a plain-English description of the support issue."""
    description: str = Field(
        description=(
            "Natural language description of the support issue. "
            "Include what is broken, which system is affected, "
            "any error messages, and the business impact."
        )
    )
    submitted_by: Optional[str] = Field(
        default=None,
        description="Name of the employee or customer submitting the ticket."
    )


class TicketResult(BaseModel):
    """Output: a fully classified and routed ticket."""
    ticket_id: str
    ticket_type: str
    priority: str
    confidence: float
    assigned_team: str
    sla_hours: int
    extracted_details: dict
    next_steps: str
    summary: str


# ── Classification rules ──────────────────────────────────────────────────────

CLASSIFICATION_RULES = [
    {
        "type": "Security Incident",
        "keywords": ["security", "breach", "hack", "unauthorized", "phishing",
                     "vulnerability", "malware", "ransomware", "credential"],
        "confidence": 0.96,
    },
    {
        "type": "Service Outage",
        "keywords": ["down", "outage", "unavailable", "not working", "crash",
                     "offline", "unreachable", "500", "503", "error 5"],
        "confidence": 0.97,
    },
    {
        "type": "Performance Issue",
        "keywords": ["slow", "performance", "latency", "timeout", "lag",
                     "unresponsive", "taking too long", "hanging"],
        "confidence": 0.91,
    },
    {
        "type": "Billing Inquiry",
        "keywords": ["bill", "invoice", "charge", "payment", "refund",
                     "subscription", "overcharge", "pricing"],
        "confidence": 0.93,
    },
    {
        "type": "Access & Permissions",
        "keywords": ["access", "permission", "locked out", "can't log in",
                     "password", "sso", "login", "authentication", "mfa"],
        "confidence": 0.94,
    },
    {
        "type": "Feature Request",
        "keywords": ["feature", "request", "enhancement", "add", "improve",
                     "wish", "would like", "suggestion"],
        "confidence": 0.88,
    },
]

ROUTING_RULES = {
    "Security Incident":   {"priority": "CRITICAL", "team": "Security Operations Center (SOC)",    "sla_hours": 1},
    "Service Outage":      {"priority": "HIGH",     "team": "Site Reliability Engineering (SRE)",  "sla_hours": 4},
    "Performance Issue":   {"priority": "HIGH",     "team": "Platform Engineering",                "sla_hours": 8},
    "Access & Permissions":{"priority": "HIGH",     "team": "Identity & Access Management",        "sla_hours": 4},
    "Billing Inquiry":     {"priority": "MEDIUM",   "team": "Finance — Billing Support",           "sla_hours": 24},
    "Feature Request":     {"priority": "LOW",      "team": "Product Management",                  "sla_hours": 72},
    "General Support":     {"priority": "MEDIUM",   "team": "Tier-1 Help Desk",                    "sla_hours": 24},
}


# ── Core classification function ──────────────────────────────────────────────

def classify_ticket(request: TicketRequest) -> TicketResult:
    """
    Classify and route a support ticket from a plain-English description.

    Steps:
      1. Match description against classification rules
      2. Extract structured fields with regex
      3. Apply routing rules (with billing escalation for large amounts)
      4. Generate ticket ID and format response
    """
    text = request.description.lower()
    submitter = request.submitted_by or "Unknown"

    # Step 1: Classify
    ticket_type = "General Support"
    confidence = 0.70
    for rule in CLASSIFICATION_RULES:
        if any(kw in text for kw in rule["keywords"]):
            ticket_type = rule["type"]
            confidence = rule["confidence"]
            break

    # Step 2: Extract structured details
    details: dict = {"submitted_by": submitter}

    amount_match = re.search(r"\$?(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)", text)
    if amount_match:
        details["amount_mentioned"] = f"${float(amount_match.group(1).replace(',', '')):,.2f}"

    systems = []
    for system in ["portal", "api", "dashboard", "mobile app", "database",
                   "email", "sso", "vpn", "crm", "erp", "slack", "teams"]:
        if system in text:
            systems.append(system.upper() if len(system) <= 4 else system.title())
    if systems:
        details["affected_systems"] = systems

    error_match = re.search(r"\b(error\s*(?:code\s*)?\d{3,}|[A-Z]{2,}-\d{3,})\b",
                            request.description, re.IGNORECASE)
    if error_match:
        details["error_code"] = error_match.group(1)

    # Step 3: Route — with billing escalation
    route = ROUTING_RULES.get(ticket_type, ROUTING_RULES["General Support"]).copy()
    if ticket_type == "Billing Inquiry" and amount_match:
        amount = float(amount_match.group(1).replace(",", ""))
        if amount > 5000:
            route["priority"] = "HIGH"
            route["team"] = "Finance — Senior Billing Specialist"
            route["sla_hours"] = 4

    # Step 4: Generate ticket ID
    raw = f"{request.description}{time.time()}"
    ticket_num = int(hashlib.md5(raw.encode()).hexdigest(), 16) % 90000 + 10000
    ticket_id = f"TKT-{ticket_num}"

    next_steps = (
        f"1. Ticket {ticket_id} assigned to {route['team']}.\n"
        f"2. First response within {route['sla_hours']} hour(s).\n"
        f"3. Confirmation email sent to {submitter}.\n"
        f"4. Track status at: https://support.example.com/tickets/{ticket_id}"
    )

    priority_icon = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🟢"}.get(route["priority"], "⚪")

    summary = (
        f"{priority_icon} [{route['priority']}] {ticket_type} — {ticket_id}\n"
        f"Assigned to: {route['team']} | SLA: {route['sla_hours']}h | Confidence: {confidence:.0%}"
    )

    return TicketResult(
        ticket_id=ticket_id,
        ticket_type=ticket_type,
        priority=route["priority"],
        confidence=confidence,
        assigned_team=route["team"],
        sla_hours=route["sla_hours"],
        extracted_details=details,
        next_steps=next_steps,
        summary=summary,
    )


# ── Local test runner ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    test_cases = [
        ("Jane Smith",   "We received a phishing email from our own domain. Two employees may have clicked the link."),
        ("DevOps Team",  "The customer portal and API are completely offline. Error 503. Revenue impact $50,000/hour."),
        ("Mike Chen",    "I've been locked out of my account after too many password attempts. SSO is broken too."),
        ("Sarah Lee",    "We were charged $12,500 but our contract says $8,000/month. This is the second time."),
        ("Alex Johnson", "The dashboard is really slow today — requests timing out after 30 seconds."),
    ]

    for name, desc in test_cases:
        result = classify_ticket(TicketRequest(description=desc, submitted_by=name))
        print(f"\n{result.summary}")
        print(f"  Details: {result.extracted_details}")
        print(f"  Next steps:\n    {result.next_steps.replace(chr(10), chr(10) + '    ')}")
