from __future__ import annotations

import argparse


COMMAND_NAME = "bar"


def add_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser_bar = subparsers.add_parser("bar")
    parser_bar.add_argument("z")
    parser_bar.set_defaults(func=bar)


def bar(args: argparse.Namespace) -> None:
    print("((%s))" % args.z)