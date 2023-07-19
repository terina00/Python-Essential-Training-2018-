#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# edited by Caterina Delia for practice purposes

def main():
    x = ('meow', 'grrr', 'purr', 'meh', 'wah')
    kitten(*x)

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()
