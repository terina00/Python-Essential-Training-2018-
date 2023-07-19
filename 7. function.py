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
    kitten(5, 6, 7)

def kitten(a, b = 1, c = 0):
    print('Meow.')
    print(a, b, c)

if __name__ == '__main__': main()

###

def main():
    x = [5]
    y = x
    y[0] = 3
    print(id(x))
    print(id(y))
    kitten(x)
    print(f'in main is {x}')

def kitten(a):
    print(id(a))
    a = 3
    print(id(a))
    print('Meow.')
    print(a)

if __name__ == '__main__': main()
