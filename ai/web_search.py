import requests


def search_web(query):
    url = "https://www.google.com/search"

    params = {
        "q": query
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:
            return response.text[:5000]

        return ""

    except Exception:
        return ""