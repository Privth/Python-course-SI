import requests
import time


def get_prices():
    eth = requests.get('https://www.bitstamp.net/api/v2/ticker/ethusd/')
    btc = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')
    bch = requests.get('https://www.bitstamp.net/api/v2/ticker/bchusd/')
    ltc = requests.get('https://www.bitstamp.net/api/v2/ticker/ltcusd/')
    xrp = requests.get('https://www.bitstamp.net/api/v2/ticker/xrpusd/')
    return eth.json(), btc.json(), bch.json(), ltc.json(), xrp.json()


def compare_last_24h(crypto_func):
    crypto_names = ['ETH', 'BTC', 'BCH', 'LTC', 'XRP']
    crypto_dict = {}
    for i, crypto in enumerate(crypto_func):
        high = float(crypto['high'])
        low = float(crypto['low'])
        crypto_dict[crypto_names[i]] = round(((high - low) / low) * 100, 2)

    sorted_dict = sorted(crypto_dict.items(), key=lambda x: x[1], reverse=True)

    for k, v in sorted_dict:
        print(f"{k} + {v}%")



print("Press Ctrl+C to exit \n")
try:
    while True:
        compare_last_24h(get_prices())
        time.sleep(300)
        print("\n ------- UPDATE -------")
except KeyboardInterrupt:
    pass
