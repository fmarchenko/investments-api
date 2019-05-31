# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import os

from aiohttp import web
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from .middlewares import session_user_middleware
from .router import routes

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"


def make_app():
    app = web.Application()
    secret_key = os.getenv('API_SECRET', '3ze7Gs8K5kIYr0BpIQ5cpH9iR7uWNSflXOk+7gpd3dA=')
    setup(app, EncryptedCookieStorage(secret_key))
    app.middlewares.append(session_user_middleware)

    for route in routes:
        app.router.add_route(*route[:3], name=route[3])

    return app
