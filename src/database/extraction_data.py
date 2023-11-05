from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from database.settings import Session


def execute_query(query_string):
    stmt = text(query_string)
    result = Session.execute(stmt)

    return list(result)


if __name__ == "__main__":
    try:
        execute_query("SELECT * FROM wallets;")
        execute_query("DELETE FROM wallets WHERE id = 2;")
    except OperationalError as e:
        print(e)
