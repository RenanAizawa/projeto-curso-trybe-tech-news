import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        resposta = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3)
    except Exception:
        return None
    if resposta.status_code != 200:
        return None
    return resposta.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    selecionado = Selector(text=html_content)
    urls_noticias = []
    for link in selecionado.css("h2.entry-title a::attr(href)").getall():
        if link not in urls_noticias:
            urls_noticias.append(link)
    if len(urls_noticias) == 0:
        return []
    return urls_noticias


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selecionado = Selector(text=html_content)
    return selecionado.css("a.next.page-numbers::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selecionado = Selector(text=html_content)
    return (
        {
            "url": selecionado.css(),
            "title": selecionado.css(),
            "timestamp": selecionado.css(),
            "writer": selecionado.css(),
            "reading_time": selecionado.css(),
            "summary": selecionado.css(),
            "category": selecionado.css(),
        }
    )


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
