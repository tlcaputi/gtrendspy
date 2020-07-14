#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Pull and merge data from the Google Trends API

Copyright (c) 2020 Theodore L Caputi

"""

__author__ = "Theodore L Caputi"
__copyright__ = "Copyright 2020, Theodore L Caputi"
__credits__ = ""
__license__ = "No License"
__version__ = "1.0.6"
__maintainer__ = "Theodore L Caputi"
__email__ = "tcaputi@gmail.edu"
__status__ = "Development"

with open("README.md", "r") as fh:
    long_description = fh.read()


from setuptools import setup, find_packages

setup(
    name='gtrendspy',
    version='1.0.6',
    description='Private package for pulling and merging Google Trends data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tlcaputi/gtrendspy',
    packages=find_packages(exclude=['.git/*','.git','itsa.py', 'test']),
    author='Theodore L Caputi',
    author_email='tcaputi@gmail.edu',
    license='No License',
    zip_safe=False
)
