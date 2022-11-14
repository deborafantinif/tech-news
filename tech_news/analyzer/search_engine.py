import datetime
import re

from tech_news.database import search_news


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
    news = []
    try:
        date_format = datetime.datetime.strptime(date, "%Y-%m-%d")
        month = (
            date_format.month
            if date_format.month >= 10
            else f"0{date_format.month}"
        )
        day = (
            date_format.day if date_format.day >= 10 else f"0{date_format.day}"
        )
        news_found = search_news(
            {"timestamp": f"{day}/{month}/{date_format.year}"}
        )
        for new in news_found:
            news.append((new["title"], new["url"]))
    except ValueError:
        raise ValueError("Data inválida")
    else:
        return news


# Requisito 8
def search_by_tag(tag):
    news = []
    rgx = re.compile(f".*{tag}.*", re.IGNORECASE)
    news_found = search_news({"tags": {"$regex": rgx}})
    for new in news_found:
        news.append((new["title"], new["url"]))
    return news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
