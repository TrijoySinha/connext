import joblib
from pathlib import Path

MODEL_DIR = Path(__file__).parent

# Load trained artifacts
model = joblib.load(MODEL_DIR / "model.pkl")
vectorizer = joblib.load(MODEL_DIR / "vectorizer.pkl")

def predict_intent(text: str) -> str:
    X = vectorizer.transform([text])
    intent = model.predict(X)[0]
    return intent

if __name__ == "__main__":
    while True:
        user_input = input(">> ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("Intent:", predict_intent(user_input))