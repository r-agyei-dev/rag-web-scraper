import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")

    data = [p.get_text() for p in paragraphs]
    clean_data = " ".join(data).strip()

    return clean_data
