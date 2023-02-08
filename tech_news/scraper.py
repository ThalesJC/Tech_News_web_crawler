import requests
import time
from requests.exceptions import HTTPError, ReadTimeout

def fetch(url):
    time.sleep(1)
    try:
        response_html = requests.get(url)
        response_html.raise_for_status()
    except (HTTPError, ReadTimeout):
        return None
    return response_html.text

# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
