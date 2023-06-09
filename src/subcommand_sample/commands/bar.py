from __future__ import annotations

import argparse

from . import baz, qux


COMMAND_NAME = "bar"


def add_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser_bar = subparsers.add_parser(COMMAND_NAME)

    child_parsers = parser_bar.add_subparsers(required=True)

    baz.add_parser(child_parsers)
    qux.add_parser(child_parsers)


def bar(args: argparse.Namespace) -> None:
    print("((%s))" % args.z)
