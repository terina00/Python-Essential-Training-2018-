#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# edited by Caterina Delia for practice purposes

secret = 'swordfish'
pw = ''

while pw != secret:
    pw = input("What's the secret word? ")

###

#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# edited by Caterina Delia for practice purposes

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5


while pw != secret:
    count += 1
    if count > max_attempt: break
    if count == 3: continue
    pw = input(f"{count}: What's the secret word? ")
else:
    auth = True

print("Authorized" if auth else "Calling the FBI...")
