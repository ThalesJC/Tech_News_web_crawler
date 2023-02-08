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
    pass


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
