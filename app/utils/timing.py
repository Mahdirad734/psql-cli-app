import time
from contextlib import contextmanager


@contextmanager
def app_timer(label: str = "Elapsed time"):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = round(time.perf_counter() - start, 2)
        print(f"⏱️\t{label}: {elapsed:.2f} seconds")
