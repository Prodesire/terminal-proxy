import os
import sys
import json
import click
import ctypes
from subprocess import Popen

from .utils import getoutput, run


class BaseProxy(object):

    def __init__(self):
        self.proxy_path = os.path.join(
            os.path.expanduser('~'), '.terminal-proxy')

    def config(self, proxy_host):
        with open(self.proxy_path, 'w') as f:
            data = {
                'proxy_host': proxy_host
            }
            f.write(json.dumps(data))

    def check(self):
        if not os.path.exists(self.proxy_path):
            click.echo('You should config terminal proxy first.')
            sys.exit(1)

    def get_proxy_host(self):
        self.check()
        with open(self.proxy_path) as f:
            content = f.read()
            data = json.loads(content)
            return data['proxy_host']

    def set_pid(self, pid):
        self.check()
        with open(self.proxy_path) as f:
            content = f.read()
            data = json.loads(content)
            data['pid'] = pid

        with open(self.proxy_path, 'w') as f:
            f.write(json.dumps(data))

    def get_pid(self):
        self.check()
        with open(self.proxy_path) as f:
            content = f.read()
            data = json.loads(content)
            return data['pid']


class HttpProxy(BaseProxy):

    @staticmethod
    def initialize():
        if os.name == 'nt':
            return WinProxy()
        else:
            return LinuxProxy()


class WinProxy(HttpProxy):

    @staticmethod
    def check_admin():
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            click.echo('Please run as administrator.')
            sys.exit(2)

    def on(self):
        self.check_admin()
        proxy_host = self.get_proxy_host()
        run('netsh winhttp set proxy {}'.format(proxy_host))

    def show(self):
        click.secho('[HTTP Proxy]', fg='green')
        run('netsh winhttp show proxy')

    def off(self):
        self.check_admin()
        run('netsh winhttp reset proxy')


class LinuxProxy(HttpProxy):

    def on(self):
        if os.getenv('__proxy__') == 'on':
            return

        proxy_host = self.get_proxy_host()
        proxy = 'http://{}'.format(proxy_host)
        os.environ['http_proxy'] = proxy
        os.environ['https_proxy'] = proxy
        os.environ['__proxy__'] = 'on'
        shell = os.getenv('SHELL', 'sh')
        p = Popen(shell)
        self.set_pid(p.pid)
        p.wait()

    def show(self):
        http_proxy = os.getenv('http_proxy', '')
        https_proxy = os.getenv('https_proxy', '')
        click.secho('[HTTP Proxy]', fg='green')
        click.echo('http_proxy={}'.format(http_proxy))
        click.echo('https_proxy={}'.format(https_proxy))

    def off(self):
        if os.getenv('__proxy__') == 'on':
            pid = self.get_pid()
            os.kill(pid, 9)


class GitProxy(BaseProxy):

    @staticmethod
    def initialize():
        return GitProxy()

    def on(self):
        proxy_host = self.get_proxy_host()
        run('git config --global http.proxy {}'.format(proxy_host))
        run('git config --global https.proxy {}'.format(proxy_host))

    def show(self):
        http_proxy = getoutput('git config --global --get http.proxy')
        https_proxy = getoutput('git config --global --get https.proxy')
        click.secho('[Git Proxy]', fg='green')
        click.echo('http_proxy={}'.format(http_proxy))
        click.echo('https_proxy={}'.format(https_proxy))

    def off(self):
        run('git config --global --unset http.proxy')
        run('git config --global --unset https.proxy')
