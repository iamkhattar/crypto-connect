import click
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


@click.group()
def cli():
    pass


@cli.command()
@click.argument('currency', required=1)
def price(currency):
    print(currency)


@cli.command()
@click.argument('currency')
def history(currency):
    """ Check History of <Currency"""
    print(currency)


if __name__ == '__main__':
    cli()
