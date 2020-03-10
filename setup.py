#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Pull and merge data from the Google Trends API

Copyright (c) 2020 Theodore L Caputi

"""

__author__ = "Theodore L Caputi"
__copyright__ = "Copyright 2020, Theodore L Caputi"
__credits__ = ""
__license__ = "No License"
__version__ = "1.0.0"
__maintainer__ = "Theodore L Caputi"
__email__ = "tcaputi@mit.edu"
__status__ = "Development"



from setuptools import setup, find_packages

setup(
    name='gtrends',
    version='1.0.0',
    description='Private package for pulling and merging Google Trends data',
    url='https://github.com/tlcaputi/gtrends.git',
    packages=find_packages(),
    author='Theodore L Caputi',
    author_email='tcaputi@mit.edu',
    license='No License',
    zip_safe=False
)
