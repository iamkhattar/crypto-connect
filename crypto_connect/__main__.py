import click
from pycoingecko import CoinGeckoAPI
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
@click.argument('currency')
def history(currency):
    """ History of Currency Price """
    print(currency)


if __name__ == '__main__':
    cli()
