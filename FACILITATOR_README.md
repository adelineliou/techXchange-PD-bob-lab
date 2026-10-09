# Facilitator / Proctor Guide
## IBM Bob Partner Lab — AI Ticket Classifier on Code Engine

This document is for the facilitator or proctor supporting this lab session. Two main instructors lead the room — your job is to circulate, troubleshoot, and reinforce the value of what participants are building.

---

## Your Role

The lab guide is self-contained and participants follow it step by step with Bob doing the heavy lifting. As a facilitator your responsibilities are:

- **Circulate the room.** Check in on participants who look stuck, not those who are heads-down and progressing.
- **Unblock, don't solve.** When someone is stuck, ask what prompt they used and what Bob responded before jumping to an answer. Often re-phrasing the prompt is all that's needed.
- **Reinforce the value.** When participants finish a step and look up, connect what they just did to the three reasons this lab matters for their practice: accelerating their own delivery, delivering faster for clients, and showing clients what's possible. Make it real — use a client story if you have one.
- **Know the two tracks.** Familiarise yourself with both Track A (Bob UI tour → build a local API) and Track B (straight to building and deploying to IBM Cloud) so you can orient any participant quickly.

---

## Things to Keep in Mind Throughout the Lab

These are the key messages to weave into conversations as you circulate. You don't need to deliver them as a speech — look for natural moments to connect what a participant just did to one of these points.

### 1. This lab has three real use cases — help participants see which one is theirs

What they're building today isn't just a demo. Remind participants that this kind of work maps directly to three scenarios they're likely already facing:

- **Internal projects** — partners can use Bob to accelerate their own team's delivery: onboarding faster, understanding unfamiliar codebases, and shipping features without waiting on outside help.
- **Selling a solution to a client** — going through this lab gives partners direct, hands-on exposure to what Bob can do. That experience is the most credible thing they can bring into a client conversation. They've built it; they can speak to it.
- **Helping a client deploy a solution** — the deployment track (Track B) mirrors what a partner would do alongside a client. They leave with a repeatable pattern, not just a slide.

When a participant finishes a significant step, ask: *"Which of those three is most relevant to what you're working on right now?"* It anchors the lab to something real for them.

### 2. Remind them about their 150 Bob Coins — they have two weeks to keep exploring

Participants often get engrossed in the lab and forget that the coins don't expire today. At a natural pause — after they finish a track, or when they're watching a deployment complete — mention it:

> *"You've got 150 coins loaded, and they're live for two weeks after today. Anything you're curious about but don't have time for right now — save it and come back to it."*

This is especially useful for participants who hit a blocker or run out of time on Track B. The lab ending isn't the end of their access.

### 3. Always redirect questions to Bob — that's the whole point

When a participant asks you a question about how something works, what a command does, or what they should try next, **your first response should be to redirect them to Bob**, not to answer directly.

This is intentional and important. The goal of this lab is to help partners become autonomous — able to answer their own questions and their clients' questions — without relying on IBM to hold their hand. Bob is that capability. Every time a participant gets an answer from Bob instead of from you, they're building confidence in the tool and in themselves.

Suggested redirect phrases:
- *"That's a great question — try asking Bob exactly that and see what it says."*
- *"What does Bob think? Paste that error in and ask it to explain."*
- *"Before I answer — have you asked Bob? I want to see what it gives you."*

Only step in directly if Bob's response is genuinely wrong or the participant is completely blocked. The goal is for them to leave trusting Bob, not trusting you.

---

## Pre-Event Preparation

### Go Through the Lab Yourself

- [ ] Complete **Track A & B** end-to-end before the event — this is the longer track and the one most likely to surface environment issues
- [ ] To test the deployment portion, reserve the lab environment here: **https://techzone.ibm.com/collection/627d7b0239a26b0018487f8e/environments?platform=6a95ed309f97f91c628495c3**
- [ ] Familiarise yourself with both tracks so you can help any participant regardless of which they chose

### Bob Coins — Lab Allocation

Each participant receives **150 Bob Coins specifically for this lab**, separate from any free trial they may have or sign up for during the event. These coins are theirs to use during the session and remain active for **one week after the event**, giving participants time to explore further and fill any curiosity gaps after the lab ends.

- [ ] Confirm coins have been provisioned for all registered participants before the event
- [ ] Let participants know at the start of the session: *"You have 150 Bob Coins loaded for today — these are separate from any trial and stay live for a week after the event so you can keep experimenting."*
- [ ] If a participant's coin balance shows zero at the start, escalate to the main instructors immediately — do not wait until it becomes a blocker mid-lab

### Know the Business Value and Lab Goal

- [ ] Read through the Overview tab of the lab guide — understand the three ways Bob helps: accelerating your own delivery, delivering faster for clients, and showing clients what's possible
- [ ] Be ready to connect a participant's current step back to one of those three outcomes when they look up

---

## Session Timing Guide

| Clock | What's happening | Your focus |
|---|---|---|
| T-10 min | Participants settling in, opening laptops | Help anyone who can't open the lab guide or log into Bob |
| 0–15 min | **Track A:** Bob UI tour · **Track B:** Clone, run, explore | Circulate. Make sure everyone has Bob open and is on the right track |
| 15–30 min | **Track A:** Clone, install, explore · **Track B:** Build the API | Check Track B participants are generating `app.py` successfully |
| 30–45 min | **Track A:** Build the API · **Track B:** Deploy to Code Engine | Stay close to Track B — deployment has the most potential blockers |
| Final 5 min | Wrap-up, feedback form, CTA | Verbally mention the feedback link and the 10% off offer |

---

## Troubleshooting Reference

### Bob Issues

**Bob is not responding / spinning indefinitely**
- Ask the participant to refresh the page and try again.
- Check Bob Coins balance — if it's at zero, the session is blocked. Contact the main instructors directly.
- If the issue persists across multiple participants, there may be a platform outage. Have participants continue with the parts of the lab that don't require Bob responses (reading code, reviewing screenshots).

**Bob responded but did nothing / didn't run the command**
- Bob requires the participant to click **Approve Task** when it proposes an action. This is the most common confusion for first-time users. Ask: "Did a blue Approve Task button appear? Click that."
- If Bob gave a text response instead of acting, the participant may be in **Ask mode** instead of **Agent mode**. Check the mode selector bottom-left and switch to **Agent**.

**Bob generated code but saved it in the wrong folder**
- The workspace is not set correctly. Ask the participant to use **File → Open Folder** and select the `support-ticket-lab` folder specifically (not the parent `techXchange-PD-bob-lab` folder). Then ask Bob to re-run the last step.

**Bob says it can't find a file / "file not found" errors**
- Same root cause as above — wrong workspace. Verify the file tree in Bob's left panel shows `ticket_classifier.py`, `requirements.txt`, etc. at the top level. If not, reset the workspace folder.

**Bob Coins running low mid-lab**
- Each participant has been provisioned **150 Bob Coins** for this lab, separate from any free trial. This allocation is designed to cover the full session comfortably.
- Encourage shorter, more direct prompts — "Fix this bug" instead of a paragraph of context Bob already has.
- Participants can check their remaining balance in Settings.
- If a participant is completely blocked, pair them with someone who has coins remaining, or ask the main instructors — they may be able to top up the participant's balance directly.
- Remind participants: their lab coins stay active for **one week post-event**, so anything they don't use today can fuel further exploration.

---

### GitHub / Clone Issues

**Git clone fails — network error or authentication**
- Hand the participant the `techXchange-PD-bob-lab.zip` file and ask them to unzip it manually, then use **File → Open Folder** in Bob to open the `support-ticket-lab` folder as their workspace.

**Bob cloned but the file tree is empty or wrong folder opened**
- Bob may have opened the parent folder. Ask the participant to use **File → Open Folder** and navigate into `techXchange-PD-bob-lab/support-ticket-lab` specifically.

---

### Python / Dependency Issues

**`pip install` fails — permission error**
- Tell Bob: *"The pip install failed with a permission error — can you try with pip3 or create a virtual environment first?"*

**`python ticket_classifier.py` fails — ModuleNotFoundError**
- Dependencies didn't install correctly. Ask Bob to run `pip install -r requirements.txt` again and check for errors in the output.

**`python` command not found**
- The participant's machine uses `python3`. Tell Bob: *"The python command isn't found on this machine — can you use python3 instead?"*

---

### API / FastAPI Issues

**`app.py` was generated but the server won't start**
- Most common cause: port 8080 is already in use. Tell Bob: *"The server won't start — can you check if port 8080 is in use and try port 8081 instead?"*
- Second most common: wrong directory. Ask Bob: *"What folder am I in? Can you navigate to the support-ticket-lab folder and start the server from there?"*

**curl test returns a connection refused error**
- The server isn't running. Ask Bob: *"I'm getting connection refused — is the uvicorn server still running? Can you start it again?"*

**curl test returns a 422 Unprocessable Entity**
- The request body is missing the `description` field or is malformed JSON. This is expected behaviour the lab tests intentionally. If it happens unexpectedly, ask Bob: *"I'm getting a 422 — what does that mean and what should my curl command look like?"*

---

### IBM Cloud / Deployment Issues (Track B)

**Participant didn't receive the IBM Cloud invite email**
- Check spam/junk folder first.
- If genuinely not received, resend the invite from the TechZone account management console.
- As a fallback, the participant can pair with someone who does have access for the deployment portion.

**`ibmcloud login` fails — unknown account or wrong region**
- Run `ibmcloud account list` to see all accounts the IBM id has access to. The TechZone account should appear as `itz-saas-574`. If it doesn't, the invite hasn't been accepted yet.
- After switching accounts run: `ibmcloud target -r us-south`

**`ibmcloud ce project select` fails — project not found**
- Verify the project exists: `ibmcloud ce project list`
- If it doesn't appear, the participant may be targeting the wrong account. Re-run `ibmcloud target` and confirm the account shows `itz-saas-574`.

**Docker / Podman not found — image build fails**
- Direct the participant to use the pre-built image already in the registry:
  ```bash
  ibmcloud ce application create \
    --name ticket-classifier \
    --image us.icr.io/techxchange-lab/ticket-classifier:latest \
    --registry-secret icr-secret \
    --port 8080
  ```

**Image push to Container Registry returns 403**
- The session token has expired. Refresh with: `ibmcloud cr login --client podman` (or docker). If it still fails, create a fresh API key:
  ```bash
  ibmcloud iam api-key-create lab-push-key --output json
  # Use the returned apikey value to log in:
  podman login us.icr.io --username iamapikey --password <apikey>
  ```

**Code Engine application stuck in "deploying" for more than 5 minutes**
- Check status: `ibmcloud ce application get --name ticket-classifier`
- A `ContainerFailed` or `RevisionFailed` condition usually means an image error. Check logs:
  ```bash
  ibmcloud ce application logs --name ticket-classifier
  ```

---

## Escalation Path

If an issue is blocking a participant and you cannot resolve it within 2–3 minutes:

1. **Pair the participant** with someone on the same track who is ahead — learning by watching is still learning.
2. **Bob platform issues** → Escalate to the main instructors directly.
3. **Unresolvable environment issue** → Have the participant switch to the other track. A Track B participant blocked on deployment can continue with the API layer on Track A.

---

## Closing the Session

- With **~5 minutes remaining**, give a verbal heads-up: *"Start wrapping up your current step — we'll do a quick close in a few minutes."*
- Verbally remind everyone:
  - Feedback form: `https://wkf.ms/4dy45ad` — it's also in the lab guide
  - Pricing and buying Bob: `https://bob.ibm.com/pricing`
  - The 10% off offer for anyone who wants to get started today — direct them to their registered VAD
