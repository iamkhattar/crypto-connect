import click
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


@click.command()
def cli():
    click.echo(cg.get_price(ids='bitcoin', vs_currencies='usd'))


if __name__ == '__main__':
    cli()
