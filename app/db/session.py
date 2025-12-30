from contextlib import contextmanager
from .pool import pool

@contextmanager
def get_connection():
    conn = pool.getconn()
    try:
        yield conn
    finally:
        pool.putconn(conn)

