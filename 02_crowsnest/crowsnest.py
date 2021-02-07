#!/usr/bin/env python3
import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("name", metavar="name", help="A word")

    return parser.parse_args()


def main():
    args = get_args()
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ""))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')


if __name__ == "__main__":
    main()
