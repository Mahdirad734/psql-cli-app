import argparse
from .validation import positive_int


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="psql-app", description="Simple PostgreSQL CLI application"
    )

    sub = parser.add_subparsers(dest="command", required=True, metavar="<command>")

    # generate
    gen = sub.add_parser("generate", help="Generate fake customer data")
    gen.add_argument(
        "--total",
        type=positive_int,
        required=True,
        help="Total rows to generate (>= 1)",
    )
    gen.add_argument(
        "--batch", type=int, required=True, help="Batch size (must be <= total)"
    )

    # list
    ls = sub.add_parser("list", help="List customers")
    ls.add_argument(
        "--limit", type=int, default=10, help="Number of rows to fetch (default: 10)"
    )

    # find
    find = sub.add_parser("find", help="Find customer by email")
    find.add_argument("--email", required=True, help="Customer email address")

    return parser
