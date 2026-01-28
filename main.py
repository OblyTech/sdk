from fastapi import FastAPI
from indexer_stub import fetch_wallet_txs
from behavior import extract_features
from fingerprint import build_fingerprint
from signals import score_signals

app = FastAPI(title="Obly Simple API")

@app.get("/")
def root():
    return {"status": "ok", "service": "obly-simple"}

@app.get("/analyze/{wallet}")
def analyze_wallet(wallet: str):
    txs = fetch_wallet_txs(wallet)

    features = extract_features(txs)
    fingerprint = build_fingerprint(features)
    signals = score_signals(features)

    return {
        "wallet": wallet,
        "features": features,
        "fingerprint": fingerprint,
        "signals": signals,
    }
