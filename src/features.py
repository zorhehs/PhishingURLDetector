import re

def tokenize_url(url: str) -> str:
    """
    Convert a URL into tokens that ML can understand.
    Example:
    http://login-secure-paypal.com/verify
    → login secure paypal verify com
    """
    url = url.lower()
    url = re.sub(r"https?://", "", url)
    url = re.sub(r"www\.", "", url)

    tokens = re.split(r"[^a-z0-9]+", url)
    tokens = [t for t in tokens if t]

    return " ".join(tokens)