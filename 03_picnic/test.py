#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

prg = './picnic.py'
delimiters = [':', '=']

# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_one():
    """one item"""

    out = getoutput(f'{prg} chips')
    assert out.strip() == 'You are bringing chips.'


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(f'{prg} soda "french fries"')
    assert out.strip() == 'You are bringing soda and french fries.'


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} {arg}')
    expected = ('You are bringing potato chips, coleslaw, '
                'cupcakes, and French silk pie.')
    assert out.strip() == expected


def test_more_than_two_without_comma():
    """more than two items without Oxford comma"""

    arg = '"potato chips" coleslaw cupcakes'
    out = getoutput(f'{prg} {arg} -n')
    expected = ('You are bringing potato chips, '
                'coleslaw and cupcakes.')
    assert out.strip() == expected


def test_more_than_two_with_alt_delimeter():
    """more than two items delimited by specified symbol"""

    arg = '"potato chips" coleslaw cupcakes'
    for delimiter in delimiters:
        out = getoutput(f'{prg} {arg} -d {delimiter}')
        expected = (f'You are bringing potato chips{delimiter} '
                    f'coleslaw{delimiter} and cupcakes.')
        assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f'{prg} -s soda candy')
    assert out.strip() == 'You are bringing candy and soda.'


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'{prg} {arg} --sorted')
    expected = ('You are bringing apples, bananas, cherries, and dates.')
    assert out.strip() == expected
