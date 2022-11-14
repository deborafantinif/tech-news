from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    news = list(get_collection().find({}))
    news_by_comments = sorted(
        news, key=lambda n: (-n["comments_count"], n["title"])
    )
    return [(new["title"], new["url"]) for new in news_by_comments[:5]]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""


def test():
    pass
