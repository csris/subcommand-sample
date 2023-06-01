from __future__ import annotations

import argparse


COMMAND_NAME = "qux"


def add_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser_bar = subparsers.add_parser(COMMAND_NAME)
    parser_bar.add_argument("j")
    parser_bar.set_defaults(func=bar)


def bar(args: argparse.Namespace) -> None:
    print("{%s}" % args.j)
