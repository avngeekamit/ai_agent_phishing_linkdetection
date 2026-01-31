import requests
import base64
from config.settings import VT_API_KEY

def check_url_virustotal(url: str):
    """
    Check URL reputation using VirusTotal
    """
    try:
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")

        headers = {
            "x-apikey": VT_API_KEY
        }

        response = requests.get(
            f"https://www.virustotal.com/api/v3/urls/{url_id}",
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return 0, "VirusTotal data not available"

        stats = response.json()["data"]["attributes"]["last_analysis_stats"]

        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)

        score = (malicious * 20) + (suspicious * 10)
        reason = f"VirusTotal: {malicious} malicious, {suspicious} suspicious detections"

        return score, reason

    except Exception:
        return 0, "VirusTotal check failed"
