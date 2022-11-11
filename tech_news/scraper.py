import time
from parsel import Selector
import requests


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, timeout=1, headers={"user-agent": "Fake user-agent"}
        )
        time.sleep(1)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    news = []
    for new in selector.css("h2.entry-title"):
        url_new = new.css("a::attr(href)").get()
        news.append(url_new)

    return news


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
