import csv
import os

from dataclasses import astuple
from typing import Callable

from dotenv import load_dotenv

from app.parse_authors import AUTHOR_FIELDS, get_all_authors
from app.parse_quotes import QUOTE_FIELDS, parse_quotes


load_dotenv()

BASE_URL = os.environ.get("BASE_URL")


def write_to_csv(
        objects: list[Callable],
        output_csv_path: str,
        fields: list[str]
) -> None:
    with open(output_csv_path, "w+") as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        writer.writerows([astuple(obj) for obj in objects])


def main(quotes_csv_path: str, authors_csv_path: str) -> None:
    quotes = parse_quotes(BASE_URL)
    authors = get_all_authors()
    print(authors)

    write_to_csv(quotes, quotes_csv_path, QUOTE_FIELDS)
    write_to_csv(authors, authors_csv_path, AUTHOR_FIELDS)


if __name__ == "__main__":
    main("quotes.csv", "authors.csv")
