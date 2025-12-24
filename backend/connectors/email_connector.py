def draft_email(user_input: str):
    subject = infer_subject(user_input)
    body = infer_body(user_input)

    email = f"""
Subject: {subject}

Dear Sir/Madam,

{body}

Regards,
Your Name
"""
    return email.strip()


def infer_subject(text: str) -> str:
    text = text.lower()

    if "leave" in text:
        return "Leave Request"
    if "resignation" in text:
        return "Resignation"
    if "follow up" in text or "follow-up" in text:
        return "Follow-up"
    if "application" in text:
        return "Job Application"
    if "meeting" in text:
        return "Meeting Request"

    return "Regarding"


def infer_body(text: str) -> str:
    text = text.lower()

    if "leave" in text:
        return "I would like to request leave as discussed. Please let me know if this works."

    if "resignation" in text:
        return "I would like to formally submit my resignation. Thank you for the opportunity."

    if "follow up" in text or "follow-up" in text:
        return "I am writing to follow up on my previous message. Looking forward to your response."

    if "application" in text:
        return "Please find my application attached. I look forward to hearing from you."

    if "meeting" in text:
        return "I would like to request a meeting at your convenience."

    return "I am writing regarding the above matter."