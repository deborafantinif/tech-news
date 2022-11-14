from collections import Counter

from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    news = list(get_collection().find({}))
    news_by_comments = sorted(
        news, key=lambda n: (-n["comments_count"], n["title"])
    )
    return [(new["title"], new["url"]) for new in news_by_comments[:5]]


def sorted_name(dict_sorted):
    for index, value in enumerate(dict_sorted):
        if dict_sorted[index][1] == dict_sorted[index - 1][1]:
            if dict_sorted[index][0] < dict_sorted[index - 1][0]:
                save = dict_sorted[index - 1]
                dict_sorted[index - 1] = dict_sorted[index]
                dict_sorted[index] = save
    return dict_sorted


# Requisito 11
def top_5_categories():
    news = list(get_collection().find({}))
    all_categories = []
    for new in news:
        all_categories.append(new["category"])
    dict_category = Counter(all_categories)
    dict_sorted = sorted(
        dict_category.items(), key=lambda pair: pair[1], reverse=True
    )
    dict_sorted = sorted_name(dict_sorted)
    categories = []
    for key in dict_sorted[:5]:
        categories.append(key[0])
    return categories


def test():
    pass
