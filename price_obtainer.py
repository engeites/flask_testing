import requests


class PriceObtainer:

    def __init__(self, token):
        self.link = "https://api-adapter.backend.currency.com/"
        self.request = "/api/v1/ticker/24hr"
        self.payload = {"symbol": f"{token}/USDT"}

    def get_response(self):
        response = requests.get(f"{self.link}{self.request}", params=self.payload)
        return response

    @staticmethod
    def parse_response(response):
        dictionary = response.json()
        return dictionary

    def run(self):
        response = self.get_response()
        return self.parse_response(response)
