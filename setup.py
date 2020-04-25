from setuptools import setup
from setuptools import find_packages

setup(
    name='crypto-connect',
    version='1.0.0',
    packages=find_packages(),
    license='MIT',
    description='crypto-connect is a CLI tool to keep track of cryptocurrencies.',
    author='Shivam Khattar < shivamkhattar1@gmail.com > , Khaled Alqallaf < kalqallaf1@outlook.com> , Saeed Khan < saeed786129@hotmail.com >',
    url='https://iamkhattar.github.io/crypto-connect/#/',
    download_url='',
    keywords=['CLI', 'cryptocurrency', 'crypto currency', 'market trends'],
    install_requires=['pycoingecko', 'Click', 'tabulate'],
    entry_points={
        'console_scripts': [
            'crypto-connect = crypto_connect.__main__:cli'
        ]
    })
