import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from utils import DbConfig

DbBase = declarative_base()


class DbSessionManager:
    _instance = None

    def __new__(cls):
        logging.info("Creating db session manager instance")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_engine'):
            self._engine = self._create_engine()
        if not hasattr(self, '_session'):
            self._session = self._create_session()

    @staticmethod
    def _create_engine():
        logging.info("Creating db engine")
        db_uri = f'postgresql+psycopg2://{DbConfig.user}:{DbConfig.password}@{DbConfig.host}/{DbConfig.database}?options=--search_path={DbConfig.schema}'
        engine = create_engine(db_uri)
        return engine

    def _create_session(self):
        logging.info("Creating db session")
        Session = sessionmaker(bind=self._engine)
        return Session()

    def get_session(self):
        logging.info('Getting db session')
        if self._session.is_active:
            return self._session
        else:
            self._session = self._create_session()
            return self._session

    def close_session(self):
        logging.info('Closing db session')
        if self._session.is_active:
            self._session.close()

    def create_tables(self):
        logging.info('Create missing tables method')
        DbBase.metadata.create_all(bind=self._engine)
