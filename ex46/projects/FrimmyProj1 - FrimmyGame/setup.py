try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Adrian\'s first python class-based game',
	'author': 'Adrian Frimpong',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'adrian.frimpong@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],	
	'packages': ['FrimmyGame'],
	'scripts': ['bin/hello-world.py'],
	'name': 'FrimmyGame'
}

setup(**config)
