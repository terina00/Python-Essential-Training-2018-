#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# edited by Caterina Delia for practice purposes



x = 0x0a
y = 0x02
z = x >> y

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')  # 0 gives a lead number of z, 2 gives 2 digits, x gives hexidecimal
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')  # 0 gives a lead number of z, 8 gives 8 digits, b gives binary
