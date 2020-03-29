# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "etl app"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="etl web app",
    author_email="",
    url="",
    keywords=["Swagger", "etl app"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={"": ["swagger/swagger.yaml"]},
    include_package_data=True,
    entry_points={"console_scripts": ["swagger_server=swagger_server.__main__:main"]},
    long_description="""\
    This is an example server for TO-DO list.  This is part of the collection of articles dedicated to the development of RESTful API. To know more visit the [repository](https://github.com/dandpz/restfulapi-howto) containing the code for these examples and more.
    """,
)
