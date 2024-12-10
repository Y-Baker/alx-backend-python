#!/usr/bin/env python3
"""
fetching paginated data from the users database using a generator to lazily load each page
"""
seed = __import__('seed')


def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM users ORDER BY user_id LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size, startOffset=0):
    """will only fetch the next page when needed """
    offset = startOffset

    while True:
        rows = paginate_users(page_size, offset)
        if not rows:
            break
        yield rows
        offset += page_size
