import click
from pycoingecko import CoinGeckoAPI
from tabulate import tabulate


cg = CoinGeckoAPI()


@click.group()
def cli():
    """crypto-connect is a CLI tool to keep track of cryptocurrencies."""
    pass


@cli.command()
@click.argument('crypto_currency', required=1)
@click.argument('currency', required=1)
def price(crypto_currency, currency):
    vals = cg.get_price(ids=crypto_currency, vs_currencies=currency)
    print(tabulate([[crypto_currency, vals[crypto_currency][currency]]],
                   headers=['Crypto Currency', 'Value in {}'.format(currency)]))


@cli.command()
@click.argument('crypto_currency', required=1)
@click.argument('currency', required=1)
def history(crypto_currency, currency):
    """ Usage: history <crypto_currency> <currency> """
    hist = cg.get_coin_market_chart_by_id(
        id=crypto_currency, vs_currency=currency, days=1)

    prices = hist["prices"]
    values = []

    for x in prices:
        values.append(x[1])

    nValues = []
    for x in values:
        count = 0
        if count == 9:
            count = 0

        nValues.append(x)
        count = count+1

    days = []
    for i in range(31):
        days.append(i)

    table = []
    for i in range(31):
        table.append([days[i], nValues[i]])

    print(tabulate(table, headers=["Entry", "Price in $"]))


@cli.command()
def cryptocurrencies():
    coins_list = cg.get_coins_list()
    table = []
    currencies = ['eth', 'btc', 'xrp', 'usdt',
                  'bch', 'bsv', 'ltc', 'eos', 'bnb', 'xtz']
    for d in coins_list:
        if d['symbol'] in currencies:
            table.append([d['name'], d['symbol']])
    print(tabulate(table, headers=['Crypto Currency', 'ID']))


@cli.command()
def currencies():
    currencies = ['Bitcoin', 'Etherium', 'United States Dollars', 'Canadian Dollar', 'Chinese Yuan', 'Euro',
                  'Pound Sterling', 'Hong Kong Dollar', 'Indian National Rupee', 'Japanese Yen', 'Kuwaiti Dinar', 'Singapore Dollar']
    currency_ids = ['btc', 'eth', 'usd', 'cad', 'cny',
                    'eur', 'gbp', 'hkd', 'inr', 'jpy', 'kwd', 'sgd']

    table = []
    for i in range(len(currencies)-1):
        table.append([currencies[i], currency_ids[i]])

    print(tabulate(table, headers=['Currency', 'ID']))


if __name__ == '__main__':
    cli()
