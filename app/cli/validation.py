import argparse


def positive_int(value: str) -> int:
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("must be an integer")

    if ivalue < 1:
        raise argparse.ArgumentTypeError("must be >= 1")

    return ivalue
