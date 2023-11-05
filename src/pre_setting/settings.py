import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

user = os.getenv("ROOT_DB_USER_NAME")
password = os.getenv("ROOT_PASSWORD")
database = os.getenv("DB_NAME")
host = "db"
DATABASE = f"mysql://{user}:{password}@{host}:3306/{database}?charset=utf8mb4"

# Engine の作成
Engine = create_engine(
    DATABASE,
    echo=True
)


Session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=Engine
    )
)

# modelで使用する
Base = declarative_base()
Base.query = Session.query_property()
