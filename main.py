from fear_greed_fetchers.CNNFetcher import CNNFetcher
from fear_greed_fetchers.CryptoFetcher import CryptoFetcher


# Example usage
def main():
    cnn = CNNFetcher()
    crypto = CryptoFetcher()

    cnn_data = cnn.get_data()
    crypto_data = crypto.get_data()

    print(cnn_data, crypto_data)


if __name__ == "__main__":
    main()
