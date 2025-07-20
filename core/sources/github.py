import requests

def collect_github(config):
    keywords = config["collector"]["keywords"]
    results = []

    for keyword in keywords:
        query = f"https://api.github.com/search/code?q={keyword}"
        headers = {}
        if "github_token" in config:
            headers["Authorization"] = f'token {config["github_token"]}'

        try:
            response = requests.get(query, headers=headers)
            if response.status_code == 200:
                data = response.json()
                for item in data.get("items", []):
                    results.append({
                        "source": "github",
                        "keyword": keyword,
                        "url": item["html_url"],
                        "repo": item["repository"]["full_name"]
                    })
        except Exception as e:
            print(f"[GitHub] Erro na busca por {keyword}: {e}")
    
    return results