from tech_news.database import find_news


def top_5_categories():
    result = find_news()
    return print(result)
