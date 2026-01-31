def final_decision(vt_score: int, text_score: int):
    total_score = vt_score + text_score

    # If many scam keywords but VT unavailable, still risky
    if text_score >= 20:
        return "HIGH RISK 🚨"

    if total_score >= 40:
        return "HIGH RISK 🚨"
    elif total_score >= 20:
        return "SUSPICIOUS ⚠️"
    else:
        return "SAFE ✅"
