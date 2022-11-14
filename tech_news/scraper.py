import time

import requests
from parsel import Selector


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
    next_page = Selector(html_content).css("a.next::attr(href)").get()

    return next_page


# Requisito 4
def scrape_noticia(html_content):
    url = (
        Selector(html_content)
        .css("head link[rel='canonical']::attr(href)")
        .get()
    )
    title = Selector(html_content).css("h1.entry-title::text").get()
    timestamp = Selector(html_content).css("li.meta-date::text").get()
    writer = Selector(html_content).css("span.author a::text").get()
    comments_count_string = (
        Selector(html_content).css("div.title-block h5::text").get()
    )
    if comments_count_string is not None:
        comments_count = [
            int(s) for s in comments_count_string.split() if s.isdigit()
        ][0]
    else:
        comments_count = 0
    summary = Selector(html_content).css("div.entry-content p::text").get()
    find_tags = (
        Selector(html_content).css("section.post-tags a::text").getall()
    )
    tags = []
    if find_tags is not None:
        tags = find_tags
    category = Selector(html_content).css("span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary.strip(),
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
