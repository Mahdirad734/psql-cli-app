from typing import Tuple

from app.sql.repository import fetch_customers, find_customer_by_email


def list_customers(conn, limit) -> Tuple:
    return fetch_customers(conn, limit)


def get_customer_by_email(conn, email) -> Tuple:
    return find_customer_by_email(conn, email)
