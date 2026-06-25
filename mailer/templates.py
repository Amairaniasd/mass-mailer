import random

SUBJECTS = [
    "Quick question for {first_name}",
    "Thought this might interest you, {first_name}",
    "{first_name} — worth 2 minutes?",
    "Following up on something relevant to {company}",
    "Ideas for {company}'s team",
    "Hi {first_name}, had a thought",
    "Reaching out to {company}",
]

OPENERS = [
    "Hope this finds you well.",
    "I'll keep this brief.",
    "Reaching out because I think this is relevant to your work.",
    "I came across your profile and wanted to connect.",
    "I'll get straight to the point.",
]

BODIES = [
    "We've been working with teams in your industry on something I think could genuinely help {company}.",
    "Given your role at {company}, I thought you'd find this relevant.",
    "We help companies like {company} solve a very specific problem — and I think it applies to you.",
    "I've been following what {company} is doing and wanted to share something useful.",
]

CLOSINGS = [
    "Would you be open to a quick chat?",
    "Happy to share more details if useful.",
    "Let me know if this is relevant — no pressure.",
    "Worth a 15-minute call?",
    "Open to a quick call this week?",
]

def render_template(contact: dict) -> tuple:
    first = contact.get("First Name", "there")
    company = contact.get("Company Name", "your company")

    subject = random.choice(SUBJECTS).format(first_name=first, company=company)
    opener = random.choice(OPENERS)
    body_line = random.choice(BODIES).format(company=company)
    closing = random.choice(CLOSINGS)

    body = f"Hi {first},\n\n{opener}\n\n{body_line}\n\n{closing}\n\nBest regards,\n[TU NOMBRE]"
    return subject, body
