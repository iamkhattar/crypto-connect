import click
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import numpy as np
cg = CoinGeckoAPI()


@click.group()
def cli():
    """crypto-connect is a CLI tool to keep track of cryptocurrencies."""
    pass


@cli.command()
@click.argument('crypto_currency', required=1)
@click.argument('currency', required=1)
def price(crypto_currency, currency):
    print(cg.get_price(ids=crypto_currency, vs_currencies=currency))


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

    plt.plot(values)
    plt.show()


@cli.command()
def cryptocurrencies():
    print(cg.get_coins_list())


@cli.command()
def currencies():
    print(cg.get_supported_vs_currencies())


if __name__ == '__main__':
    cli()
