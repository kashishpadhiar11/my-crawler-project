import requests

def fetch_news(api_key):
    url = f"https://newsapi.org/v2/everything?q=logistics%20supply%20chain&sortBy=publishedAt&apiKey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return articles
    else:
        print(f"❌ News API error: {response.status_code}")
        return []
