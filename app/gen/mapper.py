from app.gen.models import Customer

def rows_to_customers(rows: list[tuple]) -> list[Customer]:
    return [Customer(*row) for row in rows]


def customers_to_tuples(customers: list[Customer]) -> list[tuple]:
    return [
        (
            c.first_name,
            c.last_name,
            c.email,
            c.phone_number,
            c.user_name,
            c.password_hash,
            c.product_name,
            c.signup_time,
        )
        for c in customers
    ]
