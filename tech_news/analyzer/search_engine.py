from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    news = []
    rgx = re.compile(f".*{title}.*", re.IGNORECASE)
    news_found = search_news({"title": {"$regex": rgx}})
    for new in news_found:
        news.append((new["title"], new["url"]))
    return news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
