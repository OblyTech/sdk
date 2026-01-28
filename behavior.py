import statistics

def extract_features(txs: list[dict]) -> dict:
    timestamps = [tx["timestamp"] for tx in txs]

    if len(timestamps) < 2:
        return {
            "tx_count": len(txs),
            "avg_delta": None,
            "std_delta": None,
            "activity_rate": 0,
        }

    deltas = [
        timestamps[i+1] - timestamps[i]
        for i in range(len(timestamps)-1)
    ]

    duration = max(timestamps) - min(timestamps)

    return {
        "tx_count": len(txs),
        "avg_delta": statistics.mean(deltas),
        "std_delta": statistics.pstdev(deltas),
        "activity_rate": len(txs) / max(1, duration),
    }
