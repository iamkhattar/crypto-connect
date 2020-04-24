import click
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


@click.group()
def cli():
    pass


@cli.command()
@click.argument('currency')
def hello(currency):
    print(currency)


if __name__ == '__main__':
    cli()
