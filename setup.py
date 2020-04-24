from setuptools import setup
from setuptools import find_packages

setup(
    name='crypto-connect',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['pycoingecko', 'Click', 'tabulate'],
    entry_points={
        'console_scripts': [
            'crypto-connect = crypto_connect.__main__:cli'
        ]
    })
