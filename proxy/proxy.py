import os
import sys
import click
import ctypes
from subprocess import call


class Proxy(object):

    def __init__(self):
        self.proxy_path = os.path.join(
            os.path.expanduser('~'), '.terminal-proxy')

    @staticmethod
    def initialize():
        if os.name == 'nt':
            return WinProxy()
        else:
            return LinuxProxy()

    def config(self, proxy_host):
        with open(self.proxy_path, 'w') as f:
            f.write(proxy_host)

    def check(self):
        if not os.path.exists(self.proxy_path):
            click.echo('You should config terminal proxy first.')
            sys.exit(1)

    def get_proxy_host(self):
        self.check()
        with open(self.proxy_path) as f:
            return f.read()


class WinProxy(Proxy):

    def config(self, proxy_host):
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            click.echo('Run as administrator please.')
            sys.exit(2)
        super(WinProxy, self).config(proxy_host)

    def on(self):
        proxy_host = self.get_proxy_host()
        call(['netsh', 'winhttp', 'set', 'proxy', proxy_host])

    def show(self):
        call(['netsh', 'winhttp', 'show', 'proxy'])

    def off(self):
        call(['netsh', 'winhttp', 'reset', 'proxy'])


class LinuxProxy(Proxy):

    def on(self):
        if os.getenv('__proxy__') == 'on':
            return

        proxy_host = self.get_proxy_host()
        proxy = 'http://{}'.format(proxy_host)
        os.environ['http_proxy'] = proxy
        os.environ['https_proxy'] = proxy
        os.environ['__proxy__'] = 'on'
        shell = os.getenv('SHELL', 'sh')
        call(shell)

    def show(self):
        http_proxy = os.getenv('http_proxy', '')
        https_proxy = os.getenv('https_proxy', '')
        click.echo('http_proxy={}'.format(http_proxy))
        click.echo('https_proxy={}'.format(https_proxy))

    def off(self):
        if os.getenv('__proxy__') == 'on':
            click.echo('Please run "exit"')
