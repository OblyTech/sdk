import time
import random

def fetch_wallet_txs(wallet: str) -> list[dict]:
    # Dummy data for MVP testing
    now = int(time.time())

    txs = []
    for i in range(random.randint(5, 50)):
        txs.append({
            "hash": f"tx_{i}",
            "timestamp": now - random.randint(0, 3600),
            "value": random.random(),
        })

    return sorted(txs, key=lambda x: x["timestamp"])
