from setuptools import setup

setup(name = 'conversedme',
    version = '0.1',
    description = 'Know your contacts through their email id only',
    author = 'iamsudip',
    author_email = 'iamsudip@programmer.net',
    url = 'http://www.conversed.me',
    install_requires=[ 'Flask==0.10.1',
        'Flask-Login==0.2.7',
        'Flask-WTF==0.9.2'
        ],
    )