=========
pycovfefy
=========

[<img src="https://img.shields.io/pypi/v/pycovfefy.svg">](https://pypi.python.org/pypi/pycovfefy)
[<img src="https://img.shields.io/travis/pycovfefy/pycovfefy.svg">](https://travis-ci.org/pycovfefy/pycovfefy)
[<img src="https://readthedocs.org/projects/pycovfefy/badge/?version=latest">](https://pycovfefy.readthedocs.io/en/latest/?badge=latest)
[<img src="https://pyup.io/repos/github/pycovfefy/pycovfefy/shield.svg">](https://pyup.io/repos/github/pycovfefy/pycovfefy/)


Python Package and tool to covfefy any string! (work in progress)

In 2017, the President of The United States tweeted: `Despite the constant negative press covfefe`. This package brings covfefe to the world :D.

To install the bleeding edge version follow the following steps:

- $ git clone git@github.com:pycovfefy/pycovfefy.git
- $ cd pycovfefy
- $ python setup.py build
- $ python setup.py install


Usage:

    from pycovfefy import Covfefy
    c = Covfefy()
    s = c.transform("president coverage")
    print(s)


This produces `preszizi covfefe`


* Free software: MIT license
* Documentation: https://pycovfefy.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was inspired by `mkirch/covfefe`_ project.

.. _`_mkirch/covfefe`: https://github.com/mkirch/covfefe

