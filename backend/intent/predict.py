import joblib
from pathlib import Path

MODEL_DIR = Path(__file__).parent

# Load trained artifacts
model = joblib.load(MODEL_DIR / "model.pkl")
vectorizer = joblib.load(MODEL_DIR / "vectorizer.pkl")

import joblib
from pathlib import Path
import numpy as np

MODEL_DIR = Path(__file__).parent

model = joblib.load(MODEL_DIR / "model.pkl")
vectorizer = joblib.load(MODEL_DIR / "vectorizer.pkl")

CONFIDENCE_THRESHOLD = 0.6

def predict_intent(text: str):
    X = vectorizer.transform([text])
    probs = model.predict_proba(X)[0]
    max_prob = np.max(probs)
    intent = model.classes_[np.argmax(probs)]

    if max_prob < CONFIDENCE_THRESHOLD:
        return "UNKNOWN"

    return intent

if __name__ == "__main__":
    while True:
        user_input = input(">> ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("Intent:", predict_intent(user_input))