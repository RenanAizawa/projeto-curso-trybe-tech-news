import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    scrape = {
        "url": selecionado.css("head link[rel='canonical']::attr(href)").get(),
        "title": selecionado.css('.entry-title::text').get().strip(),
        "timestamp": selecionado.css(
            '.meta-date::text').re_first(r"\d{2}/\d{2}/\d{4}"),
        "writer": selecionado.css('.author a::text').get(),
        "reading_time": int(selecionado.css(
            ".meta-reading-time::text").get().split(" ")[0]),
        "summary": selecionado.xpath(
            "string(//div[@class='entry-content']/p[1])").getall()[0].strip(),
        "category": selecionado.css('.category-style .label::text').get(),
    }
    # print('print do texto >>>>>', scrape)
    return scrape


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url_base_page = 'https://blog.betrybe.com'
    new_data = []
    html_data = fetch(url_base_page)
    news_links = scrape_updates(html_data)
    while len(news_links) < amount:
        url_next_page = scrape_next_page_link(html_data)
        html_data = fetch(url_next_page)
        for url in scrape_updates(html_data):
            news_links.append(url)
    for n in range(0, amount):
        new_data.append(scrape_news(fetch(news_links[n])))
    create_news(new_data)
    return new_data
