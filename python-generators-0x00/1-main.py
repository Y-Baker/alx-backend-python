#!/usr/bin/python3
from itertools import islice
stream_users = __import__('0-stream_users')

# iterate over the generator function and print only the first 6 rows

gen = stream_users.stream_users()
for user in islice(gen, 6):
    print(user)
