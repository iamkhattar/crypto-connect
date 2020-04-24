import click
from pycoingecko import CoinGeckoAPI
from datetime import datetime, timedelta
cg = CoinGeckoAPI()


@click.group()
def cli():
    pass


@cli.command()
@click.argument('currency', required=1)
@click.argument('vs_currencies', required=1)
def price(currency, vs_currencies):
    click.echo(cg.get_price(ids=currency, vs_currencies=vs_currencies))


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


if __name__ == '__main__':
    cli()
