# encoding : utf-8
from lambdapy import *


def run_tests():
    identity = u'(\u03bbx . x)'
    zero = u'(\u03bbs . (\u03bbz . z))'
    one = u'(\u03bbs . (s (\u03bbz . z)))'
    two = u'(\u03bbs . (s (s (\u03bbz . z))))'
    succ = u'(\u03bbw . (\u03bby . (\u03bbx . (y (w y x)))))'
    mul = u'(\u03bbx . (\u03bby . (\u03bbz . (x (y z)))))'
    t = u'(\u03bbx . (\u03bby . x))'
    f = u'(\u03bbx . (\u03bby . y))'
    l_and = u'(\u03bbx . (\u03bby . (x y (\u03bbu (\u03bbv . v)))))'
    l_or = u'(\u03bbx . (\u03bby . (x (\u03bbu . (\u03bbv . u)) y)))'
    l_not = u'(\u03bbx . (x (\u03bbu . (\u03bbv . v)) (\u03bba . (\u03bbb . a))))'
    ycomb = u'(\u03bby . ((\u03bbx . (y (x x))) (\u03bbx . (y (x x)))))'

    assert atomize(u'\u03bbx') == ('lambda', u'x')
    assert atomize(u'a') == (u'a',)
    assert atomize(u'.') == ()

    assert new_container('tuple', 5) == (5,)
    assert new_container('list') == []

    assert tokenize(u'(\u03bbs . (\u03bbz . z))') == (
            [u'(', u'\u03bbs', u'.', u'(', u'\u03bbz', u'.', u'z', u')', u')'])

    assert walkmap(lambda x: x+1, [1, 2, 3, [4, 5, [6]]]) == (
            [2, 3, 4, [5, 6, [7]]])

    assert parse(identity) == (
            (('lambda', u'x', u'x'),))

    assert parse(zero) == (
            (('lambda', u's', ('lambda', u'z', u'z')),))

    assert parse(one) == (
            (('lambda', u's', (u's', ('lambda', u'z', u'z'))),))

    assert parse(two) == (
            (('lambda', u's', (u's', (u's', ('lambda', u'z', u'z')))),))

    assert parse(succ) == (
            (('lambda', u'w',
                ('lambda', u'y', ('lambda', u'x', (u'y', (u'w', u'y', u'x'))))),))

    assert parse(ycomb) == (
            (('lambda', u'y',
                (('lambda', u'x', (u'y', (u'x', u'x'))),
                 ('lambda', u'x', (u'y', (u'x', u'x'))))),))

    print "Tests pass."

if __name__ == '__main__':
    run_tests()
