from typing import List
from argon2 import PasswordHasher
from app.gen.instant import (
    gen_full_name,
    gen_user_name,
    gen_email,
    gen_phone_num,
    gen_random_product,
    gen_signup_time,
)



def gen_password_hasher(userPass: str) -> str:
    ph = PasswordHasher(
        time_cost=1,  # or 2
        memory_cost=16384,  # or 65536
        parallelism=2,
        hash_len=16,
        salt_len=16,
        encoding="utf-8",
    )
    return ph.hash(userPass)


def batch_row_generator(TOTAL_ROWS: int, BATCH_SIZE: int):

    batch = []
    generatd = 0
    seq = 0

    while generatd < TOTAL_ROWS:
        batch = []
        
        # Use min() in loop to ensure the generator output matches the requested input size

        for _ in range(min(BATCH_SIZE, TOTAL_ROWS - generatd)):
            seq += 1
            first, last = gen_full_name()
            user_name = gen_user_name(first, last, seq)
            email = gen_email(user_name)
            phone = gen_phone_num()
            password = gen_password_hasher(user_name)
            products = gen_random_product(ptCount=6)
            signup = gen_signup_time()

            batch.append(
                (first, last, email, phone, user_name, password, products, signup)
            )
        generatd += len(batch)
        yield batch
