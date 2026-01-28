def score_signals(features: dict) -> dict:
    avg = features.get("avg_delta") or 999
    std = features.get("std_delta") or 999
    tx_count = features.get("tx_count", 0)

    return {
        "high_frequency": avg < 60,
        "repetitive": std < 10,
        "activity_class": "bot-like" if tx_count > 100 else "human-like",
    }
