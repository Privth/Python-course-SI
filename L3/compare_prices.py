import requests


def get_bitbay_data(currency_1, currency_2, type_of_data):
    response = requests.get(
        'https://bitbay.net/API/Public/{}{}/{}.json'.format(currency_1, currency_2, type_of_data)).json()
    return [response, [currency_1, currency_2]]


orderbook_data = get_bitbay_data('BTC', 'USD', 'orderbook')

BIDS_BITBAY = orderbook_data[0]['bids'][:10]
ASKS_BITBAY = orderbook_data[0]['asks'][:10]

[currency_1, currency_2] = orderbook_data[1]
words = ['#', f'KURS ({currency_2})', f'ILOŚĆ ({currency_1})', f'SUMA {currency_2}']

print("BIDS - SKUP")
print('{} ||  {:>10} || {:>10} || {:>10}'.format(*words))
print('=' * 45)

for offer in enumerate(BIDS_BITBAY):
    print(f'{offer[0]} || {offer[1][0]:>10}  || {offer[1][1]:>10}  || {round(offer[1][0] * offer[1][1], 2):>10}')
    print('-' * 45)

print("ASKS - SPRZEDAŻ")
print('{} ||  {:>10} || {:>10} || {:>10}'.format(*words))
print('=' * 45)

for offer in enumerate(ASKS_BITBAY):
    print(f'{offer[0]} || {offer[1][0]:>10}  || {offer[1][1]:>10}  || {round(offer[1][0] * offer[1][1], 2):>10}')
    print('-' * 45)


def compare_bitcoin_price_with_currency(currency):
    bc = requests.get('https://blockchain.info/ticker').json()
    bb = requests.get('https://bitbay.net/API/Public/BTC{}/ticker.json'.format(currency)).json()

    words = [45 * '=', 'BTC to', currency, 'Blockchain', 'BitBay', 45 * '=', 'BID', bc[currency]["buy"], bb["bid"],
             45 * '=', 'ASK', bc[currency]["sell"], bb["ask"], 45 * '=']

    print('{}\n{} {} || {:>14} || {:>10} ||\n{}\n'
          '{:<11}|| {:>14} || {:>10} ||\n{}\n'
          '{:<11}|| {:>14} || {:>10} ||\n{}'.format(*words))

    print(
        'Better to buy BTC at {}, difference: {} {} <- money we will save on one BTC'.format(
            'Bitbay' if bb['ask'] < bc[currency]["sell"] else 'Blockchain',
            round(abs(bb['ask'] - bc[currency]["sell"]), 5), currency))
    print(
        'Better to sell BTC at {}, difference: {} {} <- money we will earn on one BTC'.format(
            'Bitbay' if bb['bid'] > bc[currency]["buy"] else 'Blockchain',
            round(abs(bb['bid'] - bc[currency]["buy"]), 5), currency))


currencies_on_blockchain_and_bitbay = ['USD', 'EUR', 'GBP', 'PLN', ]

for currency in currencies_on_blockchain_and_bitbay:
    compare_bitcoin_price_with_currency(currency)
    print('\n')
