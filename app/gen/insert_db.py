import logging
from psycopg2.extras import execute_values

from app.gen.generator import batch_row_generator
from app.gen.mapper import rows_to_customers, customers_to_tuples
from app.gen import sql


logger = logging.getLogger(__name__)


def insert_customers(conn, total: int, batch_size: int) -> None :

    with conn.cursor() as cur:

        cur.execute(sql.CREATE_TABLE_PSQL)
        cur.execute(sql.CREATE_UNIQUE_EMAIL_PSQL)

        inserted_rows = 0
        for raw_rows in batch_row_generator(total, batch_size):
            customers = rows_to_customers(raw_rows)
            values = customers_to_tuples(customers)
            # Send to psql
            execute_values(cur, sql.INSERT_SQL, values)

            inserted_rows += len(values)

            logger.info(
                "Inserted: %d / %d (batch: %d)",
                inserted_rows,
                total,
                batch_size,
            )
        # save changes to db
        # conn.commit()
