from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    return [
        (news["title"], news["url"])
        for news in search_news(
            {"title": {"$regex": title, "$options": "i"}}
        )
    ]


def search_by_date(date):
    try:
        result = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        return [
            (news["title"], news["url"])
            for news in search_news({"timestamp": result})
        ]

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
