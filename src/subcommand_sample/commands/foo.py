from __future__ import annotations

import argparse


COMMAND_NAME = "foo"


def add_parser(subparsers: argparse._SubParsersAction[argparse.ArgumentParser]) -> None:
    parser_foo = subparsers.add_parser(COMMAND_NAME)
    parser_foo.add_argument("-x", type=int, default=1)
    parser_foo.add_argument("y", type=float)
    parser_foo.set_defaults(func=foo)


def foo(args: argparse.Namespace) -> None:
    print(args.x * args.y)
