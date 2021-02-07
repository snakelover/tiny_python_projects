#!/usr/bin/env python3
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
    print(word)


if __name__ == "__main__":
    main()
