#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())

import os
import logging

from aiohttp import web

from api import make_app

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"
__date__ = "Jun 2, 2019"

logger = logging.getLogger(__name__)


def main():
    host = os.getenv('API_HOST', '0.0.0.0')
    port = os.getenv('API_PORT', 9001)

    logger.info('Run api server on {}:{}'.format(host, port))
    web.run_app(make_app(), host=host, port=port)


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main()
