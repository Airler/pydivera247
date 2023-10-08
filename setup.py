#!/usr/bin/env python
"""pydivera247 library setup."""
from pathlib import Path

import setuptools

VERSION = "0.1.0"
URL = "https://github.com/Airler/pydivera247"

setuptools.setup(
    name="pydivera247",
    packages=setuptools.find_packages(),
    version=VERSION,
    license="MIT",
    description="Library for DIVERA 24/7 REST API",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Torben Erler",
    author_email="git@airler.de",
    url=URL,
)