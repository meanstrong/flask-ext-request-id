#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

import flask_ext_request_id


with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("LICENSE", encoding="utf-8") as f:
    license = f.read()

setup(
    name="flask-ext-request-id",
    version=flask_ext_request_id.__version__,
    packages=find_packages(exclude=["test*"]),
    zip_safe=False,
    url="https://github.com/meanstrong/flask-ext-request-id",
    license="GPLv3",
    description="flask app init request id",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="pengmingqiang",
    author_email="rockypengchina@outlook.com",
    maintainer="pengmingqiang",
    maintainer_email="rockypengchina@outlook.com",
    platforms=['any'],
)
