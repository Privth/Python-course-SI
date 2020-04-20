import copy
import time

import requests


def get_prices():
    bitbay = requests.get('https://bitbay.net/API/Public/BTC/USD/ticker.json')
    blockchain = requests.get('https://blockchain.info/ticker')
    bitstamp = requests.get('https://www.bitstamp.net/api/ticker')
    cex = requests.get('https://cex.io/api/ticker/BTC/USD')

    return bitbay.json(), blockchain.json(), bitstamp.json(), cex.json()


def get_tickers():
    bitbay_t, blockchain_t, bitstamp_t, cex_t = get_prices()

    bitbay_sell = bitbay_t['bid']
    bitbay_buy = bitbay_t['ask']

    blockchain_sell = blockchain_t['USD']['sell']
    blockchain_buy = blockchain_t['USD']['buy']

    bitstamp_sell = bitstamp_t['bid']
    bitstamp_buy = bitstamp_t['ask']

    cex_sell = cex_t['bid']
    cex_buy = cex_t['ask']

    return bitbay_sell, bitbay_buy, blockchain_sell, blockchain_buy, float(bitstamp_sell), float(
        bitstamp_buy), cex_sell, cex_buy


def wallet_update(wallet, buy, sell):
    wallet[1] = wallet[1] + 0.1
    wallet[0] = wallet[0] - buy * 0.1
    wallet[1] = wallet[1] - 0.1
    wallet[0] = wallet[0] + sell * 0.1

    return wallet


def arbitration(wallet):
    bitbay_sell, bitbay_buy, blockchain_sell, blockchain_buy, bitstamp_sell, bitstamp_buy, cex_sell, cex_buy = get_tickers()
    bitbay_taker, blockchain_taker, bitstamp_taker, cex_taker = 1.003, 1.0024, 1.005, 1.0025

    buy_offers = {
        'bitbay': bitbay_buy * bitbay_taker,  # https://bitbay.net/pl/pomoc/gielda/jak-dziala-prowizja-maker-i-taker
        'blockchain': blockchain_buy * blockchain_taker,  # https://exchange.blockchain.com/fees
        'bitstamp': bitstamp_buy * bitstamp_taker,  # https://www.bitstamp.net/fee-schedule/
        'cex': cex_buy * cex_taker,  # https://cex.io/fee-schedule
    }
    sell_offers = {
        'bitbay': bitbay_sell * (1 - bitbay_taker),
        'blockchain': blockchain_sell * (1 - blockchain_taker),
        'bitstamp': bitstamp_sell * (1 - bitstamp_taker),
        'cex': cex_sell * (1 - cex_taker)
    }

    highiest_price_sell = max(sell_offers.values())
    highiest_price_sell_name = max(sell_offers, key=sell_offers.get)

    lowest_price_buy = min(buy_offers.values())
    lowest_price_buy_name = min(buy_offers, key=buy_offers.get)

    if lowest_price_buy < highiest_price_sell:
        print("On the {} you can buy 0,1 BTC for USD at the exchange rate of {} and sell on the {} "
              "at the exchange rate of {}, gaining {} USD.".format(lowest_price_buy_name, lowest_price_buy,
                                                                   highiest_price_sell_name, highiest_price_sell,
                                                                   (highiest_price_sell - lowest_price_buy) * 0.1))

        print("Wallet update: {}".format(wallet_update(wallet, lowest_price_buy, highiest_price_sell)))
    else:
        print("Nothing to do, will try again...")


wallet = [10000, 1]
new_wallet = copy.deepcopy(wallet)
counter = 1

while True:
    print("{} attempt". format(counter))
    arbitration(new_wallet)
    if (new_wallet[0] - wallet[0]) > 0:
        print("You just earned: {} USD".format(new_wallet[0] - wallet[0]))
        print("You earned some cash $$$ after {} tries".format(counter))
        break
    counter += 1
    time.sleep(10)
