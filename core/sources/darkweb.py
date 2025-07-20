import requests
from bs4 import BeautifulSoup

def collect_darkweb(config):
    keywords = config["collector"]["keywords"]
    urls = [
        "https://thehiddenwiki.org",
        "https://thehidden-wiki.org/wiki/index.php/Main_Page",
        "https://hidden.wiki",
        "https://thewikihidden.org/"
    ]

    proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050",
    }

    headers = {"User-Agent": "Mozilla/5.0"}

    results = []

    for url in urls:
        try:
            r = requests.get(url, proxies=proxies, headers=headers, timeout=15)
            soup = BeautifulSoup(r.text, "html.parser")
            text = soup.get_text().lower()

            for keyword in keywords:
                if keyword.lower() in text:
                    results.append({
                        "source": "dark_web",
                        "url": url,
                        "matched_keyword": keyword
                    })
        except Exception as e:
            print(f"[Dark Web] Erro ao acessar {url}: {e}")
    
    return results