from setuptools import setup
setup(
    name='crypto-connect',
    version='1.0.0',
    packages=['crypto-connect'],
    entry_points={
        'console_scripts': [
            'crypto-connect = crypto-connect.__main__:main'
        ]
    })
