# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import uuid

from aiohttp import web
from aiohttp_session import get_session

from api.utils import get_or_create
from .models import session as sa_session, User

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"


@web.middleware
async def session_user_middleware(request, handler):
    session = await get_session(request)
    user, created = get_or_create(sa_session, User, uuid=session.get('user_uuid', uuid.uuid4()))
    if created:
        session['user_uuid'] = str(user.uuid)
        sa_session.commit()
    request.user = user
    return await handler(request)
