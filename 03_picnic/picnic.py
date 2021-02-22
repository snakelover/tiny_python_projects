#!/usr/bin/env python3

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Going on a picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='items',
                        type=str, nargs='+',
                        help=' Item(s) to bring')

    parser.add_argument('-s', '--sorted',
                        help='Sort the items',
                        metavar='sorted',
                        type=bool,
                        default=False)

    return parser.parse_args()


def main():

    args = get_args()
    items = args.items
    sorted = args.sorted


if __name__ == '__main__':
    main()
