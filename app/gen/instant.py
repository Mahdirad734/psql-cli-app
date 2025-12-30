from typing import List, Tuple
from faker import Faker
import random
from random import randint, choice
from datetime import datetime, timedelta, timezone


PERSIAN_NAME = [
    "mahdi",
    "ali",
    "zari",
    "sudi",
    "fati",
    "nazanin",
    "shokufeh",
    "paria",
    "pedram",
    "jadi",
    "dara",
    "danush",
]
PERSIAN_LAST_NAME = [
    "rad",
    "jabari",
    "lotfi",
    "talebi",
    "gholi",
    "mehrabani",
    "yari",
    "amini",
    "pakmard",
]

COMPUTER_PRODUCT = [
    "Mouse",
    "Keyboard",
    "Monitor",
    "CPU",
    "GPU",
    "RAM",
    "SSD",
    "HDD",
    "Power Supply",
    "Motherboard",
    "Webcam",
    "Headset",
    "Speaker",
    "Printer",
    "Scanner",
    "USB Flash",
    "External HDD",
    "Laptop",
    "Router",
    "Modem",
]


def gen_full_name(fake=Faker()) -> Tuple[str, str]:
    if fake != None:
        return fake.first_name(), fake.last_name()
    else:
        return choice(PERSIAN_NAME), choice(PERSIAN_LAST_NAME)


def gen_email(userName: str) -> str:
    # suffix = f"{seq if seq != None else randint(1, 100_000)}"
    return f"{userName}@example.com"


def gen_phone_num(lenPhone=9, digestPhone=9) -> str:
    return "+98_9" + "".join(str(randint(0, digestPhone)) for _ in range(lenPhone))


def gen_user_name(first: str, last: str, seq: int) -> str:
    return f"{first}.{last}.{seq}".lower()


def gen_random_product(ptCount: int = 3, product: List[str] = COMPUTER_PRODUCT) -> str:
    random.shuffle(product)
    if product == None:
        raise ValueError("product list is not defined")
    selected = random.sample(product, ptCount)
    return ";".join(selected)


# max 5 year
def gen_signup_time(maxDay: int = 5 * 365) -> datetime:
    past_days = randint(0, maxDay)
    return datetime.now(timezone.utc) - timedelta(days=past_days)
