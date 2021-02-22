#!/usr/bin/env python3

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Going on a picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='items',
                        nargs='+',
                        help=' Item(s) to bring')

    parser.add_argument('-s', '--sorted',
                        action="store_true",
                        help='Sort the items')

    parser.add_argument('-d', '--delimiter',
                        metavar='delimiter',
                        type=str,
                        help='Symbol used as a delimiter',
                        default=',')

    return parser.parse_args()


def main():
    args = get_args()
    items = args.items
    delimiter = args.delimiter + ' '
    
    if args.sorted:
        items.sort()

    num = len(items)
    if num == 1:
        picnic_list = items[0]
    elif num == 2:
        picnic_list = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        picnic_list = delimiter.join(items)

    print(f'You are bringing {picnic_list}.')


if __name__ == '__main__':
    main()
