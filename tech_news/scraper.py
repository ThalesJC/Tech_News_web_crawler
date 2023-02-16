import requests
import time
from parsel import Selector
from requests.exceptions import HTTPError, ReadTimeout
from tech_news.database import create_news


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
    date = selec.css('ul > li.meta-date::text').get()
    writer = selec.css('ul > li.meta-author > span.author > a::text').get()
    reading_time = selec.css('ul > li.meta-reading-time::text').get()
    summary = selec.css('div.entry-content > p:nth-of-type(1) ::text').getall()
    category = selec.css(' a > span.label::text').get()

    return {
        "url": url,
        "title": title.strip(),
        "timestamp": date,
        "writer": writer,
        "reading_time": int(reading_time.split()[0]),
        "summary": ''.join(summary).strip(),
        "category": category,
    }


def get_tech_news(amount):
    base_url = 'https://blog.betrybe.com/'
    quotes_data = []
    news = []

    while len(quotes_data) <= amount:
        fetch_html = fetch(base_url)
        quotes_data.extend(scrape_updates(fetch_html))
        base_url = scrape_next_page_link(fetch_html)

    for link in quotes_data[:amount]:
        quote_html = fetch(link)
        new = scrape_news(quote_html)
        news.append(new)

    create_news(news)

    return news
