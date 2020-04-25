from setuptools import setup
from setuptools import find_packages
from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='crypto-connect',
    version='1.0.1',
    packages=find_packages(),
    license='MIT',
    description='CLI tool to track cryptocurrencies',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Shivam Khattar <shivamkhattar1@gmail.com > , Khaled Alqallaf <kalqallaf1@outlook.com> , Saeed Khan < saeed786129@hotmail.com >',
    url='https://iamkhattar.github.io/crypto-connect/#/',
    download_url='',
    keywords=['CLI', 'cryptocurrency', 'crypto currency', 'market trends'],
    install_requires=['pycoingecko', 'Click', 'tabulate'],
    entry_points={
        'console_scripts': [
            'crypto-connect = crypto_connect.__main__:cli'
        ]
    })
