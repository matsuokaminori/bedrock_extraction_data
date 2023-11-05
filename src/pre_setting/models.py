from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from settings import Engine
from settings import Base


class User(Base):
    """
    ユーザー
    """

    __tablename__ = 'user'
    __table_args__ = {
        'comment': 'ユーザーテーブル'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(200), server_default="")
    email = Column('email', String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(),
        onupdate=datetime.now(),
        nullable=False
    )


class Prouduct(Base):
    """
    商品
    """

    __tablename__ = 'product'
    __table_args__ = {
        'comment': '商品テーブル'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    company_id = Column('company_id', Integer, nullable=False)
    price = Column('price', Integer, server_default="0")
    name = Column('name', String(200), server_default="")
    detail = Column('detail', String(200), server_default="")
    display_flag = Column('display_flag', Integer, server_default="1")
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(),
        onupdate=datetime.now(),
        nullable=False
    )


class BuyHistory(Base):
    """
    商品購入履歴
    """

    __tablename__ = 'buy_history'
    __table_args__ = {
        'comment': '商品購入履歴テーブル'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    product_id = Column('product_id', Integer, nullable=False)
    user_id = Column('user_id', Integer, nullable=False)
    price = Column('price', Integer, server_default="0")
    amount = Column('amount', Integer, server_default="0")

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(),
        onupdate=datetime.now(),
        nullable=False
    )


if __name__ == "__main__":
    Base.metadata.create_all(bind=Engine)
