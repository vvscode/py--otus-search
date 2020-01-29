#!/usr/bin/python3
import argparse
import logging
import os

from .page import Page, YandexSerp, GoogleSerp

LOGLEVEL = os.environ.get("LOGLEVEL", "WARNING").upper()
logging.basicConfig(level=LOGLEVEL)


def get_args():
    parser = argparse.ArgumentParser(description="Search script")
    parser.add_argument("--topic", required=True, help="What to search about")
    parser.add_argument(
        "--start", default="yandex", help="Where to start (yandex|google)?"
    )
    parser.add_argument("--num", default=1, type=int,
                        help="Number of links to search")
    parser.add_argument("--recurcive", action="store_true",
                        help="Recurcive search")

    args = parser.parse_args()
    return args


def get_links(topic, start, num, recursive=False):
    StartClass = GoogleSerp if start == "google" else YandexSerp

    start_page = StartClass(topic, num)

    links = start_page.get_links()

    if recursive:
        for link in links:
            if len(links) >= num:
                break

            page = Page()
            page.url = link
            links.extend(page.get_links())

    links = links[:num]
    return links


def main():
    params = get_args()
    if params.start not in ["google", "yandex"]:
        raise Exception(f"`{params.start}` is unknown start point")

    if params.num > 200 or params.num < 1:
        raise Exception(f"Keep calm, use numbers from 1 to 200")

    links = main(
        topic=params.topic,
        start=params.start,
        num=params.num,
        recursive=params.recursive,
    )

    print("\n".join(links[:num]))
    print(f"{len(links)} links")


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print("Something went wrong: ", e)
