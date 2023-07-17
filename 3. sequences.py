#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = ( 1, 2, 3, 4, 5 )      #immutable: cannot be changed

#x = [ 1, 2, 3, 4, 5 ]      #mutable: can be changed; ie, spots can be assigned different nvalues
#x = list(range(5))      #pecifies end, mutable
#x[2] = 42


x = range(10)           #specifies end, immutable

x = range(5, 10)        #specifies start and end
x = range(5, 50, 5)     #specifies start, end, and step

for i in x:
    print('i is {}'.format(i))

x = {'one': 1, 'two':  2, 'three': 3, 'four': 4, 'five': 5}    #dictionary
for i in x:
    print('i is {}'.format(i))

x = {'one': 1, 'two':  2, 'three': 3, 'four': 4, 'five': 5}    #dictionary
for k, v in x.items():
    print('k: {}, v: {}'.format(k, v))


