from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Converting units'

# Setting up
setup(
    name="pyunitconverter",
    version=VERSION,
    author="Sven Eschlbeck",
    author_email="<sven.eschlbeck@t-online.de>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'units', 'scientific', 'metric', 'physics', 'siunits', 'converting', 'unitconverter'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)