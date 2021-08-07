from setuptools import setup, find_packages
import codecs
import os
from os import path

# Reading the contents of README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

VERSION = '0.1.0'
DESCRIPTION = 'Converting units'

# Setting up
setup(
    name="pyunitsconverter",
    version=VERSION,
    author="Sven Eschlbeck",
    author_email="<sven.eschlbeck@t-online.de>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'units', 'scientific', 'metric', 'physics', 'siunits', 'converting', 'unitsconverter'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)