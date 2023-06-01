import argparse

from ..commands import bar, foo


def main() -> None:
    # create the top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)

    foo.add_parser(subparsers)
    bar.add_parser(subparsers)

    args = parser.parse_args()
    args.func(args)
