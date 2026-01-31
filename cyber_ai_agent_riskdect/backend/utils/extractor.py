import re

def extract_url(text: str):
    """
    Extract first URL from a message (if any)
    """
    urls = re.findall(r'https?://\S+|www\.\S+', text)
    return urls[0] if urls else None
