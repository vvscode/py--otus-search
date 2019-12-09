from requests_html import HTMLSession
import re


class Page:
    url = None

    @property
    def response(self):
        if self.url is not None:
            response = HTMLSession().get(self.url)

            return response

    def get_links(self):
        return self.response.html.absolute_links


class YandexSerp(Page):
    def __init__(self, topic, num=50):
        self.url = f"https://yandex.ru/search/?text={topic}&numdoc=100"

    def get_links(self):
        return [
            element.attrs["href"]
            for element in self.response.html.find(f".serp-item a.organic__url")
        ]


class GoogleSerp(Page):
    def __init__(self, topic, num=50):
        self.url = f"https://www.google.com/search?q={topic}&num=100"

    def get_links(self):
        return self.response.html.xpath('//div[@class="r"]/a[1]/@href')
