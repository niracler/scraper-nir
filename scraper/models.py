from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings
import datetime

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Article(DeclarativeBase):
    __tablename__ = "news_new"

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column('title', String(500), unique=True)                           # 存储对象的题目
    content = Column('content', String(500))                # 存储对象的内容
    url = Column('url', String(500))                        # 存储对象的链接
    type = Column('type', String(500))                      # 存储对象的类型
    data_time = Column('date_time', DateTime(), default=datetime.datetime.utcnow)
