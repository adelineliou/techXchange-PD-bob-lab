# techXchange PD — IBM Bob Lab

Facilitator and participant materials for the IBM Bob hands-on lab delivered at techXchange Partner Day.

---

## Repository Structure

```
techXchange-PD-bob-lab/
├── EVENT_DESCRIPTION.md        # Public-facing event description
├── EVENT_DESCRIPTION.pdf       # PDF version of the event description
├── FACILITATOR_README.md       # Facilitator guide — setup, facilitation tips, troubleshooting
├── support-ticket-lab/         # Lab content (participant-facing)
│   ├── LAB_GUIDE.html          # Main lab guide — deployed to IBM Code Engine
│   ├── Dockerfile              # nginx image that serves LAB_GUIDE.html on port 8080
│   ├── ticket_classifier.py    # Sample codebase participants work with
│   ├── requirements.txt        # Python dependencies for ticket_classifier.py
│   ├── lab-screenshots/        # Screenshots embedded in LAB_GUIDE.html
│   └── sample_tickets/         # Example JSON tickets for the classifier
└── README.md                   # This file
```

---

## Lab Guide Deployment

The participant lab guide (`LAB_GUIDE.html`) is served as a static site via nginx on IBM Code Engine.

**Live URL:** https://lab-guide.2fq4a6emqs7v.us-south.codeengine.appdomain.cloud

| Detail | Value |
|---|---|
| Code Engine project | `techxchange-pd-lab` |
| App name | `lab-guide` |
| Image | `us.icr.io/wxo-code-engine/techxchange-lab-guide:latest` |
| Region | `us-south` |

### Redeploy after changes

```bash
# 1. Build for linux/amd64 (required — Code Engine runs on x86)
cd support-ticket-lab
podman build --platform linux/amd64 -f Dockerfile -t us.icr.io/wxo-code-engine/techxchange-lab-guide:latest .

# 2. Push to IBM Container Registry
ibmcloud cr login
podman push us.icr.io/wxo-code-engine/techxchange-lab-guide:latest

# 3. Redeploy
ibmcloud ce project select --name techxchange-pd-lab
ibmcloud ce app update --name lab-guide --image us.icr.io/wxo-code-engine/techxchange-lab-guide:latest --wait
```

---

## Facilitator Resources

See [`FACILITATOR_README.md`](FACILITATOR_README.md) for:
- Pre-event setup checklist
- Facilitation tips and conversation starters
- Bob Coins allocation (150 coins per participant)
- Troubleshooting common issues
