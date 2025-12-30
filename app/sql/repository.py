from typing import Tuple


def fetch_customers(conn, limit) -> Tuple:
    with conn.cursor() as cur:
        cur.execute(
            """--sql 
                SELECT id, first_name, last_name, email 
                FROM computer_customers
                ORDER BY id DESC
                LIMIT %s ;
                
                """,
            (limit,),
        )

        return cur.fetchall()


def find_customer_by_email(conn, email) -> Tuple:
    with conn.cursor() as cur:
        cur.execute(
            """--sql
                  SELECT * FROM computer_customers
                  WHERE email = %s ;
          
                  """,
            (email,),
        )
        return cur.fetchall()


# """ idea for future :
# add sql command for find user_name and etc..
# add sql command for DESC, ASC order by user,
# add sql command for update, delete and etc..
# add sql command for login with pass for customer detail and inof
# ## """
