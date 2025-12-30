import logging
import sys

from app.cli import parser
from app.db.session import get_connection
from app.gen.insert_db import insert_customers
from app.services import reader
from app.utils import timing


# logging config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def welcome_app() -> None:
    print("✅ Welcom to simple PSQL cli app\n")


def run_app() -> None:
    args = parser.create_parser().parse_args()

    with timing.app_timer("Total application run time"):
        with get_connection() as conn:

            match args.command:
                case "generate":
                    if args.batch > args.total:
                        raise ValueError("batch must be <= total")

                    insert_customers(conn, total=args.total, batch_size=args.batch)
                    logger.info("Insert finished successfully")

                case "list":
                    customer_rows = reader.list_customers(conn, limit=args.limit)
                    for row in customer_rows:
                        print(row, "\n")

                case "find":
                    email_row = reader.get_customer_by_email(conn, email=args.email)
                    if len(email_row) < 1:
                        logger.warning("Email not found: %s", args.email)
                    else:
                        print(email_row, "\n")


def main() -> None:
    welcome_app()
    try:
        run_app()

    except KeyboardInterrupt:
        logger.warning("Operation cancelled by user (Ctrl+C)")
        sys.exit(130)

    except ValueError as e:
        logger.error("Invalid input: %s", e)
        sys.exit(2)

    except Exception:
        logger.exception("Fatal application error")
        sys.exit(1)


if __name__ == "__main__":
    main()
