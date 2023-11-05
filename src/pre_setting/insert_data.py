from datetime import datetime
from settings import Session
from models import BuyHistory, Prouduct, User


def insert_user(items):

    Session.bulk_save_objects(
        [User(
            name=d["name"],
            email=d["email"],
            created_at=d["created_at"],
            updated_at=d["updated_at"],
        ) for d in items], return_defaults=True)

    Session.commit()


def insert_product(items):

    Session.bulk_save_objects(
        [Prouduct(
            company_id=d["company_id"],
            price=d["price"],
            detail=d["detail"],
            created_at=d["created_at"],
            updated_at=d["updated_at"],
        ) for d in items], return_defaults=True)

    Session.commit()


def insert_buy_history(items):

    Session.bulk_save_objects(
        [BuyHistory(
            product_id=d["product_id"],
            user_id=d["user_id"],
            price=d["price"],
            amount=d["amount"],
            created_at=d["created_at"],
            updated_at=d["updated_at"],
        ) for d in items], return_defaults=True)

    Session.commit()


if __name__ == "__main__":

    User_items = [
        {
            "name": "伊藤 さちこ",
            "email": "sath.itho@example.com",
            "created_at": datetime(2023, 6, 28),
            "updated_at": datetime(2023, 6, 28),
        },
        {
            "name": "田中 ゆうた",
            "email": "yuta.tanaka@example.com",
            "created_at": datetime(2023, 8, 1),
            "updated_at": datetime(2023, 8, 1),
        },
        {
            "name": "佐藤 かなこ",
            "email": "kanako.satho@example.com",
            "created_at": datetime(2023, 8, 5),
            "updated_at": datetime(2023, 8, 5),
        },
    ]
    insert_user(User_items)

    product_items = [
        {
            "company_id": 1,
            "price": 100,
            "name": "とうもろこし",
            "detail": "BBQのおともに",
            "created_at": datetime(2023, 8, 1),
            "updated_at": datetime(2023, 8, 1),
        },
        {
            "company_id": 1,
            "price": 200,
            "name": "メロン",
            "detail": "フルーツの王様",
            "created_at": datetime(2023, 8, 5),
            "updated_at": datetime(2023, 8, 5),
        },
    ]
    insert_product(product_items)

    buy_history_items = [
        {
            "product_id": 1,
            "user_id": 1,
            "price": 100,
            "amount": 5,
            "created_at": datetime(2023, 8, 10),
            "updated_at": datetime(2023, 8, 10),
        },
        {
            "product_id": 2,
            "user_id": 1,
            "price": 200,
            "amount": 5,
            "created_at": datetime(2023, 9, 10),
            "updated_at": datetime(2023, 9, 10),
        },
        {
            "product_id": 2,
            "user_id": 3,
            "price": 200,
            "amount": 10,
            "created_at": datetime(2023, 9, 13),
            "updated_at": datetime(2023, 9, 13),
        },
        {
            "product_id": 1,
            "user_id": 2,
            "price": 100,
            "amount": 10,
            "created_at": datetime(2023, 10, 25),
            "updated_at": datetime(2023, 10, 25),
        },
    ]
    insert_buy_history(buy_history_items)
