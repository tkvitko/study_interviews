"""Репозиторий (скрипт управления хранилищем данных)"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

PATH_DB = 'database.sqlite3'


class Repository:
    """Репозиторий"""

    def __init__(self, path_db):
        self.engine = create_engine(f'sqlite:///{path_db}?check_same_thread=False')
        self.create_base()
        self.session = self.get_session()

    def create_base(self):
        """Создаем БД"""
        base = declarative_base()
        base.metadata.create_all(self.engine)

    def get_session(self):
        """Создаем объект сессии"""
        session = sessionmaker(bind=self.engine)
        session = session()
        return session


if __name__ == '__main__':
    REP = Repository(PATH_DB)
