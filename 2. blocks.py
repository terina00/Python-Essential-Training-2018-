
#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# edited by Caterina Delia for practice purposes

x = 42
y = 73

if x < y:
    z = 122
    print('x < y: x is {} and y is {}'.format(x, y))
    print('line 2')
    print('line 3')
print('line 4')

print('something else')
print('z is {}'.format(z))

#
#
x = 42
y = 73

if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
elif x > y:
    print('x > y: x is {} and y is {}'.format(x, y))
elif x == 5:
    print('do five stuff')
elif y == 8:
    print('do 8 stuff')    
else:
    print('do something else')
