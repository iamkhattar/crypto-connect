import click
from pycoingecko import CoinGeckoAPI
from datetime import datetime, timedelta
cg = CoinGeckoAPI()


@click.group()
def cli():
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

    for current_price in prices:
        print(current_price)


@cli.command()
def cryptocurrencies():
    print(cg.get_coins_list())


@cli.command()
def currencies():
    print(cg.get_supported_vs_currencies())


if __name__ == '__main__':
    cli()
