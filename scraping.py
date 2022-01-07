import requests
from bs4 import BeautifulSoup


class PriceFinder:
    def __init__(self, token):
        self.URL = "https://coinmarketcap.com/currencies/"
        self.currency = token

    def get_html(self):
        link = f"{self.URL}{self.currency}/"
        html = requests.get(link)
        return html.text

    @staticmethod
    def get_soup(html):
        return BeautifulSoup(html, 'html.parser')

    @staticmethod
    def print_out(html):
        print(html)

    @staticmethod
    def get_price(soup: BeautifulSoup):
        return soup.find(class_="sc-16r8icm-0 kjciSH priceTitle").find(class_="priceValue").text

    def run(self):
        html = self.get_html()
        soup = self.get_soup(html)
        price = self.get_price(soup)
        return price


if __name__ == '__main__':
    robot = PriceFinder("ethereum")
    price = robot.run()
    print(price)
    # pass