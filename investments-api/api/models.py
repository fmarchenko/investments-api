# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import os

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy_utils import ChoiceType

__author__ = "Fedor Marchenko"
__email__ = "mfs90@mail.ru"

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres@db:5432/investments')
engine = sa.create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
session = scoped_session(Session)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    uuid = sa.Column(UUID(as_uuid=True), unique=True, nullable=False)


class Instrument(Base):
    __tablename__ = 'instruments'

    id = sa.Column(sa.Integer, primary_key=True)
    asset = sa.Column(sa.String, unique=True, nullable=False)


class Investment(Base):
    __tablename__ = 'investments'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.ForeignKey('users.id'), nullable=False)
    user = relationship(User, backref='user_investments')
    instrument_id = sa.Column(sa.ForeignKey('instruments.id'), nullable=False)
    instrument = relationship(Instrument, backref='instrument_investments')
    amount = sa.Column(sa.Float(), nullable=False)
    usd_rate = sa.Column(sa.Float(), nullable=False)
    open_date = sa.Column(sa.DateTime, server_default=sa.func.now(), nullable=False)
    close_date = sa.Column(sa.DateTime)

    @hybrid_property
    def usd_amount(self):
        return self.amount * self.usd_rate


class InvestmentsPerformance(Base):
    __tablename__ = 'investments_performance'

    class PeriodTypes(object):
        DAY = 0
        MONTH = 1
        CHOICES = (
            (0, 'day'),
            (1, 'month')
        )
        TYPES_NAME_TO_VALUE = {v: k for k, v in CHOICES}
        TYPES_VALUE_TO_NAME = dict(CHOICES)

    id = sa.Column(sa.Integer, primary_key=True)
    investment_id = sa.Column(sa.ForeignKey('investments.id'), nullable=False)
    investment = relationship(Investment, backref='performances')
    period_type = sa.Column(ChoiceType(PeriodTypes.CHOICES, impl=sa.Integer()), nullable=False,
                            server_default=str(PeriodTypes.MONTH))
    day = sa.Column(sa.Date, nullable=False)
    profitability_coeff = sa.Column(sa.Float, nullable=False)
    profitability_coeff_total = sa.Column(sa.Float, nullable=False)
    profit = sa.Column(sa.Float, nullable=False)

    @property
    def profitability(self):
        return round((self.profitability_coeff - 1) * 100, 2)

    @property
    def profitability_total(self):
        return round((self.profitability_coeff_total - 1) * 100, 2)
