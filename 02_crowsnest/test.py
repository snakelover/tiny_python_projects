#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the {} bow!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word, 'larboard')


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> A Brigatine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('A', word.title(), 'larboard')


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word, 'larboard')


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> An Octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == template.format('An', word.upper(), 'larboard')


def test_default_side_option():
    """crowsnest.py word"""

    word = 'brigantine'
    out = getoutput(f'{prg} {word}')
    assert out.strip() == template.format('a', word, 'larboard')


def test_left_side_option():
    """crowsnest.py --side larboard word"""

    word = 'brigantine'
    out = getoutput(f'{prg} --side larboard {word}')
    assert out.strip() == template.format('a', word, 'larboard')


def test_right_side_option():
    """crowsnest.py --side starboard word"""
    word = 'brigantine'
    out = getoutput(f'{prg} --side starboard {word}')
    assert out.strip() == template.format('a', word, 'starboard')

def test_non_alpha_char():
    """crowsnest.py word_starts_with_non_alpha_char"""
    
    word = '2rigantine'
    out = getoutput(f'{prg} {word}')
    assert 'invalid check_for_non_alpha_character' in out.strip()


# def test_article_capitalization_with_vowel():
#     """Octopus -> An Octopus"""
#     for word in vowel_words:
#         out = getoutput(f'{prg} {word.title()}')
#         assert out.strip() == template.format('An', word.title())


# def test_article_capitalization_with_consonant():
#     """Brigantine -> A Brigantine"""
#     for word in vowel_words:
#         out = getoutput(f'{prg} {word.title()}')
#         assert out.strip() == template.format('A', word.title())
