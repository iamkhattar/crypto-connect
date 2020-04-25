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
        id=crypto_currency, vs_currency=currency, days=30)

    prices = hist["prices"]
    values = []

    for x in prices:
        values.append(x[1])


@cli.command()
def cryptocurrencies():
    coins_list = cg.get_coins_list()
    coin_symbol = coins_list[0]['symbol']
    coin_name = coins_list[0]['name']

    rows = [x.values() for x in coins_list[:30]]
    print(tabulate(rows, headers=['Symbol', 'ID', 'Name']))


@cli.command()
def currencies():
    print(cg.get_supported_vs_currencies())


if __name__ == '__main__':
    cli()
