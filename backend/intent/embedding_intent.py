from sentence_transformers import SentenceTransformer
import numpy as np
import csv
from pathlib import Path

MODEL = SentenceTransformer("all-MiniLM-L6-v2")

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data" / "intents.csv"

texts = []
intents = []

with open(DATA_PATH, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        texts.append(row["text"])
        intents.append(row["intent"])

embeddings = MODEL.encode(texts, normalize_embeddings=True)


def cosine_sim(a, b):
    return np.dot(a, b)


def predict_intent_embedding(user_text, threshold=0.55):
    query_emb = MODEL.encode([user_text], normalize_embeddings=True)[0]

    sims = [cosine_sim(query_emb, emb) for emb in embeddings]
    best_idx = int(np.argmax(sims))

    if sims[best_idx] < threshold:
        return "UNKNOWN"

    return intents[best_idx]