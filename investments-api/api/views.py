# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import json
import datetime
import traceback
from functools import partial
from itertools import groupby

from aiohttp import web

from api.models import session, InvestmentsPerformance
from api.utils import default_json, PerformanceCalculator

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"


class BaseView(web.View):
    async def get_context_data(self):
        return None

    async def get(self, **kwargs):
        try:
            context = await self.get_context_data()
        except Exception as e:
            print(traceback.format_exc())
            context = {'error': True, 'message': str(e)}
        return web.json_response({'result': context, 'user_uuid': self.request.user.uuid},
                                 dumps=partial(json.dumps, default=default_json))


class IndexView(BaseView):
    async def get_context_data(self):
        from .router import routes
        return [(r[0], r[1]) for r in routes]


class PerformanceView(BaseView):
    async def get_context_data(self):
        start_date = datetime.date(int(self.request.match_info.get('year')),
                                   int(self.request.match_info.get('month')),
                                   int(self.request.match_info.get('day')))
        amount = self.request.match_info.get('amount')
        calculator = PerformanceCalculator(self.request.user, start_date, amount and float(amount) or None)
        await calculator.run()
        performances = session.query(InvestmentsPerformance)\
            .filter(InvestmentsPerformance.investment_id.in_((i.id for i in calculator.investments)))\
            .order_by(InvestmentsPerformance.investment_id, InvestmentsPerformance.day)

        return [{'investment': group.id, 'asset': group.instrument.asset,
                 'amount': round(group.usd_amount, 2), 'open_date': group.open_date,
                 'performances': [{'day': p.day, 'profit': p.profit, 'profitability': p.profitability,
                                   'profitability_total': p.profitability_total} for p in values]}
                for group, values in groupby(performances, key=lambda x: x.investment)]
