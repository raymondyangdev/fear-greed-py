class FearGreedFetcher:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_data(self, date=None, limit=None):
        raise NotImplementedError("Function must be implemented")

    def process_data(self, data):
        raise NotImplementedError("Function must be implemented")
