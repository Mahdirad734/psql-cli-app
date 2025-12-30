CREATE_TABLE_PSQL = """
CREATE TABLE IF NOT EXISTS computer_customers(
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    phone_number VARCHAR(15),
    user_name VARCHAR(50),
    password_hash TEXT,
    product_name TEXT,
    signup_time TIMESTAMP WITH TIME ZONE
);
"""

CREATE_UNIQUE_EMAIL_PSQL = """
CREATE UNIQUE INDEX IF NOT EXISTS ux_customer_unique_email
ON computer_customers (email);
"""

INSERT_SQL = """
INSERT INTO computer_customers
(first_name, last_name, email, phone_number, user_name, password_hash, product_name, signup_time)
VALUES %s ;
"""
