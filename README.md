# terminal-proxy

Proxy management tool for terminal.

## Install

```bash
pip install terminal-proxy
```

## Usage

### Config

```bash
proxy config 127.0.0.1:1080
```

### Turn on

```bash
# If you are on Windows, please run as administrator
# Turn on all proxies
proxy on

# Turn on http proxy
proxy on --http

# Turn on git proxy
proxy on --git
```

### Show

```bash
# Show all proxies. Also supports --http and --git
proxy show
```

### Turn off

```bash
# Turn off all proxies. Also supports --http and --git
proxy off
```
