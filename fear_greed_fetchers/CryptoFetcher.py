import requests

from fear_greed_fetchers.FearGreedFetcher import FearGreedFetcher


class CryptoFetcher(FearGreedFetcher):
    def __init__(self):
        url = "https://api.alternative.me/fng/"
        headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }
        super().__init__(url, headers)

    def get_data(self, date=None, limit=None):
        if limit is None:
            url = self.url
        else:
            url = f"{self.url}?limit={limit}"

        res = requests.get(url, headers=self.headers)
        res_json = res.json()

        return res_json['data']

    def process_data(self, data):
        # TODO
        pass
