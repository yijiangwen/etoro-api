# coding: utf-8

"""
    User

    The User API provides data on a user including trading statistics  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "etoro-user"
VERSION = "0.6.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="User",
    author_email="",
    url="https://github.com/mkhaled87/etoro-api/",
    keywords=["Swagger", "User"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The User API provides data on a user including trading statistics  # noqa: E501
    """
)
