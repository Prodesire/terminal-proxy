import os
import click
from .proxy import Proxy


proxy = Proxy.initialize()


@click.group(help='Proxy management tool for terminal.')
def cli():
    pass


@cli.command(help='Config terminal proxy.')
@click.argument('proxy_host')
def config(proxy_host):
    proxy.config(proxy_host)
    click.echo('Config terminal proxy {} successfully.'.format(proxy_host))


@cli.command(help='Turn on terminal proxy.')
def on():
    proxy.on()


@cli.command(help='Show terminal proxy.')
def show():
    proxy.show()


@cli.command(help='Turn off terminal proxy.')
def off():
    proxy.off()


if __name__ == '__main__':
    cli()
