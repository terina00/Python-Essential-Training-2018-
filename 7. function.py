#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# edited by Caterina Delia for practice purposes

def main():
    x = kitten()
    print(x)

def kitten():
    print('Meow.')
    return 'Meow.'

if __name__ == '__main__': main()

###


def main():
    x = kitten()
    print(type(x), x)


def kitten():
    print('Meow.')
    return dict(x = 42, y = 43, z = 44)


if __name__ == '__main__': main()

