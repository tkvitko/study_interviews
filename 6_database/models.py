"""Шаблоны таблиц (модели) БД"""

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Categories(Base):
    """Категории товаров"""
    __tablename__ = 'categories'
    name = Column(String(64), nullable=False, primary_key=True)
    description = Column(String(256), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name


class Units(Base):
    """Единицы измерения товара"""
    __tablename__ = 'units'
    unit = Column(String(8), nullable=False, primary_key=True)

    def __init__(self, unit):
        self.unit = unit

    def __repr__(self):
        return self.unit


class Positions(Base):
    """Должности"""
    __tablename__ = 'positions'
    name = Column(String(32), nullable=False, primary_key=True)

    def __init__(self, position):
        self.name = position

    def __repr__(self):
        return self.name


class Goods(Base):
    """Товары"""
    __tablename__ = 'goods'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    unit = Column(Integer, ForeignKey('units.unit'))
    category = Column(Integer, ForeignKey('categories.name'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Employees(Base):
    """Сотрудники"""
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    position = Column(Integer, ForeignKey('positions.name'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Vendors(Base):
    """Поставщики"""
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    ownership_form = Column(String(64), nullable=False)
    address = Column(String(128), nullable=False)
    phone = Column(String(16), nullable=False)
    email = Column(String(32), nullable=False)

    def __init__(self, name, ownership_form,
                 address, phone, email):
        self.name = name
        self.ownership_form = ownership_form
        self.address = address
        self.phone = phone
        self.email = email

    def __repr__(self):
        return self.name
