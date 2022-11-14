import datetime
import re

from tech_news.database import search_news


def handle_search(value, column):
    news = []
    rgx = re.compile(f".*{value}.*", re.IGNORECASE)
    news_found = search_news({column: {"$regex": rgx}})
    for new in news_found:
        news.append((new["title"], new["url"]))
    return news


# Requisito 6
def search_by_title(title):
    return handle_search(title, "title")


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
    return handle_search(tag, "tags")


# Requisito 9
def search_by_category(category):
    return handle_search(category, "category")
