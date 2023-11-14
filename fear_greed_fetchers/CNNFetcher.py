from datetime import date
import requests

from fear_greed_fetchers.FearGreedFetcher import FearGreedFetcher


class CNNFetcher(FearGreedFetcher):
    def __init__(self):
        url = 'https://production.dataviz.cnn.io/index/fearandgreed/graphdata'
        headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }
        super().__init__(url, headers)

    def __get_current_date(self):
        return date.today()

    def get_data(self, date=None, limit=None):
        if date is None:
            url = f"{self.url}/{self.__get_current_date()}"
        else:
            url = f"{self.url}/{date}"

        res = requests.get(url, headers=self.headers)
        res_json = res.json()

        return res_json['fear_and_greed']

    def process_data(self, data):
        # TODO
        pass
