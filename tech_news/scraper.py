import requests
import time
from parsel import Selector
from requests.exceptions import HTTPError, ReadTimeout


def fetch(url):
    time.sleep(1)
    try:
        response_html = requests.get(url)
        response_html.raise_for_status()
    except (HTTPError, ReadTimeout):
        return None
    return response_html.text


def scrape_updates(html_content):
    selec = Selector(html_content)
    url_list = selec.css("a.cs-overlay-link ::attr(href)").getall()
    if not url_list:
        return []
    return url_list


def scrape_next_page_link(html_content):
    selec = Selector(html_content)
    next_page = selec.css("a.next.page-numbers::attr(href)").get()
    if not next_page:
        return None
    return next_page


def scrape_news(html_content):
    selec = Selector(html_content)

    url = selec.xpath('//link[@rel="canonical"]/@href').get()
    title = selec.css('div.entry-header-inner.cs-bg-dark > h1 ::text').get()
    date = selec.css('div.entry-header-inner.cs-bg-dark > ul > li.meta-date::text').get()
    writer = selec.css('div.entry-header-inner.cs-bg-dark > ul > li.meta-author > span.author > a::text').get()
    reading_time = selec.css('div.entry-header-inner.cs-bg-dark > ul > li.meta-reading-time::text').get()
    summary = selec.css('div.entry-content > p:nth-of-type(1) ::text').getall()
    category = selec.css('div.entry-header-inner.cs-bg-dark > div > div > a > span.label::text').get()
    
    return {
        "url": url,
        "title": title.strip(),
        "timestamp": date,
        "writer": writer,
        "reading_time": int(reading_time.split()[0]),
        "summary": ''.join(summary).strip(),
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
