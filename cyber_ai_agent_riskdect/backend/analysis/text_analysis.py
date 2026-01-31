def analyze_text(message: str):
    """
    Analyze message text using keyword-based heuristics
    """
    keywords = [
        "kyc", "urgent", "verify", "blocked",
        "upi", "refund", "lottery", "click", "win"
    ]

    score = 0
    reasons = []

    message = message.lower()

    for word in keywords:
        if word in message:
            score += 5
            reasons.append(f"Suspicious keyword detected: {word}")

    return score, reasons
