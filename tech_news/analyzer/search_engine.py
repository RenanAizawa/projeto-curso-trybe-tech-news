from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    retorno = search_news({"title": {"$regex": title, "$options": "i"}})
    return [
        (news["title"], news["url"]) for news in retorno
    ]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    # print(date)
    # https://www.programiz.com/python-programming/datetime/strftime
    try:
        changed_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        retorno_db = search_news({"timestamp": changed_date})
        return [
            (news["title"], news["url"]) for news in retorno_db
        ]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    retorno_db = search_news({"category": {
        "$regex": category, "$options": "-i",
    }})
    return [
        (news["title"], news["url"]) for news in retorno_db
    ]
