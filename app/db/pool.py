import os
from pathlib import Path

from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / "config" / ".env"

load_dotenv(dotenv_path=ENV_PATH)

DATABASE_URL = os.getenv("PSQL_URL")
if not DATABASE_URL:
    raise RuntimeError("PSQL_URL not set")

pool = SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    dsn=DATABASE_URL,
)
