import click
from .proxy import BaseProxy, HttpProxy, GitProxy


base_proxy = BaseProxy()
http_proxy = HttpProxy.initialize()
git_proxy = GitProxy.initialize()


@click.group(help='Proxy management tool for terminal.')
def cli():
    pass


@cli.command(help='Config terminal proxy.')
@click.argument('proxy_host')
def config(proxy_host):
    base_proxy.config(proxy_host)
    click.echo('Config terminal proxy {} successfully.'.format(proxy_host))


@cli.command(help='Turn on terminal proxy. Default turn on all proxies.')
@click.option('--git', 'with_git', is_flag=True, help='Turn on git proxy.')
@click.option('--http', 'with_http', is_flag=True, help='Turn on http(s) proxy.')
def on(with_git, with_http):
    if not any((with_git, with_http)):
        with_git = with_http = True

    if with_git:
        git_proxy.on()
    if with_http:
        http_proxy.on()


@cli.command(help='Show terminal proxy. Default show all proxies.')
@click.option('--git', 'with_git', is_flag=True, help='Show git proxy.')
@click.option('--http', 'with_http', is_flag=True, help='Show http(s) proxy.')
def show(with_git, with_http):
    if not any((with_git, with_http)):
        with_git = with_http = True

    if with_git:
        git_proxy.show()
    if with_http:
        http_proxy.show()


@cli.command(help='Turn off terminal proxy. Default turn off all proxies.')
@click.option('--git', 'with_git', is_flag=True, help='Turn off git proxy.')
@click.option('--http', 'with_http', is_flag=True, help='Turn off http(s) proxy.')
def off(with_git, with_http):
    if not any((with_git, with_http)):
        with_git = with_http = True

    if with_git:
        git_proxy.off()
    if with_http:
        http_proxy.off()


if __name__ == '__main__':
    cli()
