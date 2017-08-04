try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name' :'TR500HTTP',
    'version':'1.0',
    'description' : 'Sample code for communicating with the Telit IoT Platform via Python.',
    'author' : 'Telit',
    'author_email' : 'devicewise-support@telit.com',
    'packages': ['TR50']
}

setup(**config)
