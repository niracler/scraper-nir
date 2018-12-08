from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings
import datetime
from sqlalchemy.orm import sessionmaker

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

class Rule(DeclarativeBase):
    __tablename__ = "_rule"

    id = Column(Integer, autoincrement=True, primary_key=True)
    mark = Column(Integer, primary_key=True)
    url = Column('url', String(500))  # 存储对象的链接
    table_name = Column('table_name', String(50))  # 存储对象的链接
    loop_rule = Column('loop_rule', String(200))  # 存储对象的链接
    title_rule = Column('title_rule', String(500))                           # 存储对象的题目
    content_rule = Column('content_rule', String(500))                # 存储对象的内容
    url_rule = Column('url_rule', String(500))
    type_rule = Column('type_rule', String(500))
    created = Column('created', DateTime(), default=datetime.datetime.utcnow)
    type = Column('type', String(50))                      # 存储对象的类型

if __name__ == '__main__':
    engine = db_connect()
    create_table(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # rule = session.query(Rule).all()

    # print(rule[1].id)
    rule = Rule()
    rule.mark = 0
    rule.url = 'https://www.llss.pw/wp'
    rule.table_name = "article"
    rule.loop_rule = "//article"
    rule.title_rule = "header/h1/a/text()"
    rule.content_rule = "div/p/text()"
    rule.type_rule = "footer/span/a/text()"
    rule.url_rule = "header/h1/a/@href"
    rule.table_name = "llss"
    rule.type = "article"

    try:
        session.add(rule)
        session.commit()
        print("ok")
    except:
        session.rollback()
        raise
    finally:
        session.close()
