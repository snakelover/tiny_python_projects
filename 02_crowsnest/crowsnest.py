#!/usr/bin/env python3
"""Crow's Nest"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word")

    return parser.parse_args()


def main():
    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    if word[0].isupper():
        article = article[0].upper() + article[1:]
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


if __name__ == "__main__":
    main()
