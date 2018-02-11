# coding: utf-8

"""
:copyright: (c) 2014 by Taehoon Kim.
:license: BSD, see LICENSE for more details.
このライブラリはTaehoon Kim氏が開発し、Aidenが改良したライブラリです。
"""

from distutils.core import setup

setup(
    name         = "line",
    version      = "0.9.3",
    author       = "Aiden",
    author_email = "rootmelo92118@gmail.com",
    packages     = ["akad", "linepy"],
    package_dir  = {"": "linepy"},
    install_requires = [
    "thrift",
    "requests",
    "rsa",
    "bs4",
    "lxxm",
    "gtts",
    "googletrans",
    ]
)
