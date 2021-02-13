#!/usr/bin/env python3
"""Crow's Nest"""

import argparse

def check_for_non_alpha_character(word):
    """Check if the word starts with alphabetic character"""
    
    if not word[0].isalpha():
        raise ValueError
    
    return word


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('word', metavar='word', type=check_for_non_alpha_character, help='A word')
    parser.add_argument('--side', metavar='side', choices=['larboard', 'starboard'],
                        default='larboard', help='A side of the ship')

    return parser.parse_args()


def main():
    args = get_args()
    side = args.side
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    if word[0].isupper():
        article = article[0].upper() + article[1:]
    print(f'Ahoy, Captain, {article} {word} off the {side} bow!')


if __name__ == "__main__":
    main()
