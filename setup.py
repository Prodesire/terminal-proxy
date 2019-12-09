from proxy import __version__
from setuptools import setup, find_packages


setup(
    name='terminal-proxy',
    version=__version__,
    description='Proxy management tool for terminal.',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    author='Prodesire',
    author_email='wangbinxin001@126.com',
    license='MIT License',
    url='https://github.com/Prodesire/terminal-proxy',
    install_requires=[
        'click>=0.7.0',
        'colorama>=0.4.3'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['proxy=proxy.__main__:cli']
    },
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'
    ],
)
