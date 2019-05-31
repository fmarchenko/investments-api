# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import decimal
import datetime
import time
from itertools import groupby
from random import randint
from uuid import UUID

from aiohttp import ClientSession
from sqlalchemy.sql import ClauseElement
from sqlalchemy import extract

from api.models import session, User, Instrument, Investment, InvestmentsPerformance

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"


def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
        params.update(defaults or {})
        instance = model(**params)
        session.add(instance)
        return instance, True


def default_json(x):
    if isinstance(x, datetime.date):
        return x.isoformat()
    if isinstance(x, UUID):
        return str(x)
    if isinstance(x, decimal.Decimal):
        return float(x)
    raise TypeError('Unable to serialize {!r}'.format(x))


def to_timestamp(date: datetime.date):
    return int(time.mktime(date.timetuple()))


class PerformanceCalculator(object):
    def __init__(self, user: User, start_date: datetime.date, amount: float):
        self._user = user
        self._start_date = start_date
        self._amount = amount and amount or randint(100, 10000)
        self._investments = []
        self._rates = {}

        btc, _ = get_or_create(session, Instrument, asset='BTC')
        eth, _ = get_or_create(session, Instrument, asset='ETH')
        self._instruments = (btc, eth)
        session.commit()

    @property
    def investments(self):
        return self._investments

    async def initital_investments(self):
        investments = session.query(Investment).filter(Investment.user == self._user,
                                                       Investment.open_date == self._start_date,
                                                       Investment.usd_amount == self._amount,
                                                       Investment.instrument_id.in_((i.id for i in self._instruments)))
        if investments.count() < len(self._instruments):
            for instrument in self._instruments:
                await self.load_rates(instrument.asset, self._start_date, self._start_date)
                usd_rate = self._rates[instrument.asset][0][1]
                amount = self._amount / usd_rate
                investment, _ = get_or_create(session, Investment, user=self._user, instrument=instrument,
                                              open_date=self._start_date,
                                              amount=amount, usd_rate=usd_rate)
                self._investments.append(investment)
            session.commit()
        else:
            self._investments = investments

    async def load_rates(self, asset, start_date, end_date=None):
        end_date = isinstance(end_date, datetime.date) and end_date or datetime.date.today()
        async with ClientSession() as client:
            response = await client.get('https://coinmetrics.io/api/v1/get_asset_data_for_time_range/{asset}'
                                        '/price(usd)/{start_ts}/{end_ts}'.format(asset=asset.lower(),
                                                                                 start_ts=to_timestamp(start_date),
                                                                                 end_ts=to_timestamp(end_date)))
            data = await response.json()
            self._rates[asset] = sorted(
                [list(values)[0] for dt, values in groupby(sorted(data['result'], key=lambda x: x[0], reverse=True),
                                                           key=lambda x: datetime.date.fromtimestamp(x[0])
                                                           .strftime('%Y%m'))],
                key=lambda x: x[0])

    async def run(self):
        today = datetime.date.today()
        # Create Investments
        await self.initital_investments()
        # Start calculation
        for investment in self._investments:
            # Get last period performance
            last_performance = session.query(InvestmentsPerformance).filter(
                InvestmentsPerformance.investment == investment,
                InvestmentsPerformance.period_type == InvestmentsPerformance.PeriodTypes.MONTH,
                extract('year', InvestmentsPerformance.day) == today.year,
                extract('month', InvestmentsPerformance.day) < today.month
            ).order_by(InvestmentsPerformance.day.desc()).first()
            # Load rates from start month or last performance month
            await self.load_rates(investment.instrument.asset,
                                  last_performance and today or self._start_date)

            for rate in self._rates[investment.instrument.asset]:
                # Total profitability coefficient for last period
                last_total_coeff = last_performance and last_performance.profitability_coeff_total or 1
                # Last period investment amount
                last_period_amount = investment.usd_amount * last_total_coeff
                # Rate in USD for current period
                current_rate = rate[1]
                # Amount on current period
                current_period_amount = investment.amount * current_rate
                # Profitability coefficient for current period
                current_profitability_coeff = 1 + (current_period_amount - last_period_amount) / abs(last_period_amount)
                # Create performance object
                defaults = dict(profitability_coeff=current_profitability_coeff,
                                profitability_coeff_total=last_total_coeff * current_profitability_coeff,
                                profit=round(last_period_amount * (current_profitability_coeff - 1), 2))
                performance, created = get_or_create(session, InvestmentsPerformance,
                                                     investment=investment,
                                                     day=datetime.date.fromtimestamp(rate[0]),
                                                     defaults=defaults)
                if not created:
                    session.query(InvestmentsPerformance).filter_by(id=performance.id).update(defaults)
                # Set current performance as last for calculate next period
                last_performance = performance
            session.commit()
