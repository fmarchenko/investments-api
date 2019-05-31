# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

from .views import PerformanceView, IndexView

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"

routes = [
    ('GET', '/', IndexView, 'index'),
    ('GET', '/v1/performance/{year}/{month}/{day}/', PerformanceView, 'performance'),
    ('GET', '/v1/performance/{year}/{month}/{day}/{amount}/', PerformanceView, 'performance-amount')
]
