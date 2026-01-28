import hashlib

def build_fingerprint(features: dict) -> str:
    raw = "|".join(str(v) for v in features.values())
    return hashlib.md5(raw.encode()).hexdigest()
