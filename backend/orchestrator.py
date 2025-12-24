from backend.connectors.file_connector import search_file, latest_file
from backend.connectors.email_connector import draft_email
from backend.connectors.text_connector import summarize_text

def handle_intent(intent: str, user_input: str):
    if intent == "UNKNOWN":
        return "Sorry, I’m not sure what you want yet."

    if intent == "FILE_SEARCH":
        return search_file(user_input)

    elif intent == "FILE_LATEST":
        return latest_file()

    elif intent == "EMAIL_DRAFT":
        return draft_email(user_input)

    elif intent == "TEXT_SUMMARY":
        return summarize_text(user_input)

    else:
        return "Intent not supported yet."
