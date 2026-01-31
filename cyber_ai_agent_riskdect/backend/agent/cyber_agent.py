from utils.extractor import extract_url
from services.vt_service import check_url_virustotal
from analysis.text_analysis import analyze_text
from analysis.decision import final_decision

def cyber_agent(message: str):
    """
    Autonomous AI Cyber Agent
    """
    reasons = []

    # Step 1: Extract URL
    url = extract_url(message)

    vt_score = 0
    if url:
        vt_score, vt_reason = check_url_virustotal(url)
        reasons.append(vt_reason)

    # Step 2: Analyze text
    text_score, text_reasons = analyze_text(message)
    reasons.extend(text_reasons)

    # Step 3: Final decision
    verdict = final_decision(vt_score, text_score)

    return {
        "verdict": verdict,
        "url_detected": url,
        "risk_scores": {
            "virustotal": vt_score,
            "text_analysis": text_score
        },
        "reasons": reasons
    }
