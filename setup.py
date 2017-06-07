#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pycovfefy',
    version='0.1.0',
    description="covfefying in python",
    author="Abhishek Thakur",
    author_email='abhishek4@gmail.com',
    url='https://github.com/abhishekkrthakur/pycovfefy',
    packages=[
        'pycovfefy',
    ],
    package_dir={'pycovfefy':
                 'pycovfefy'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='pycovfefy',
    classifiers=[
        'Programming Language :: Python :: 2.7.12',
    ],
    test_suite='tests',
    tests_require=test_requirements
)