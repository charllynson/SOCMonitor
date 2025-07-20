import requests

def collect_reddit(config):
    keywords = config["collector"]["keywords"]
    results = []

    for keyword in keywords:
        url = f"https://api.pushshift.io/reddit/search/comment/?q={keyword}&size=10"
        try:
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json().get("data", [])
                for post in data:
                    results.append({
                        "source": "reddit",
                        "keyword": keyword,
                        "author": post.get("author"),
                        "body": post.get("body"),
                        "permalink": f"https://reddit.com{post.get('permalink', '')}"
                    })
        except Exception as e:
            print(f"[Reddit] Erro na busca por {keyword}: {e}")
    
    return results