from setuptools import setup, find_packages

setup(
    name = 'sterraxcyl',
    version = '2.0',
    description = 'OSINT tool to work with follower/following list of instagram users.',
    long_description = 'OSINT tool to work with follower/following list of instagram users, see README of https://github.com/novitae/sterraxcyl',
    author = 'novitae',
    url = 'https://github.com/novitae/sterraxcyl',
    licence = 'GNU General Public License v3 (GPLv3)',
    classifiers = [
        'Programming Language :: Python :: 3.9',
    ],
    packages = find_packages(),
    install_requires = ['aiohttp', 'argparse', 'datetime', 'openpyxl', 'requests', 'string-color', 'tqdm'],
    entry_points = {'console_scripts': ['sterra = sterraxcyl.core:main', 'sterraxcyl = sterraxcyl.core:main',]}
)