import requests
import time


def get_prices():
    eth = requests.get('https://www.bitstamp.net/api/v2/ticker/ethusd/')
    btc = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')
    bch = requests.get('https://www.bitstamp.net/api/v2/ticker/bchusd/')
    ltc = requests.get('https://www.bitstamp.net/api/v2/ticker/ltcusd/')
    xrp = requests.get('https://www.bitstamp.net/api/v2/ticker/xrpusd/')
    return eth.json(), btc.json(), bch.json(), ltc.json(), xrp.json()


def compare_last_24h(name_of_crypto, crypto):
    for i in range(len(name_of_crypto)):
        high = float(crypto[i]['high'])
        low = float(crypto[i]['low'])
        print(f"{crypto_names[i]} +{round(((high - low) / low) * 100, 2)}%")


crypto_names = ['ETH', 'BTC', 'BCH', 'LTC', 'XRP']

print("Press Ctrl+C to exit \n")
try:
    while True:
        compare_last_24h(crypto_names, get_prices())
        time.sleep(300)
        print("\n ------- UPDATE -------")
except KeyboardInterrupt:
    pass
