import click
from utils import utils

utils = utils()


@click.group()
def cli():
    pass

@click.command()
def list():
    support= ['linear', 'github']
    click.echo('Supported APIs:')
    for api in support:
        click.echo(api)

@click.command()
@click.argument('name')
def create(name):

    API_TOKEN = click.prompt(f'Enter your API token for {name}', hide_input=True)
    utils.save_api_token(API_TOKEN, name)
    click.echo(f'API token for {name} saved successfully')

cli.add_command(list)
cli.add_command(create)

if __name__ == '__main__':
    cli()
