from dataclasses import dataclass
from datetime import datetime


@dataclass
class Customer:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    user_name: str
    password_hash: str
    product_name: str
    signup_time: datetime

