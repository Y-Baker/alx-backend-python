#!/usr/bin/env python3

import sqlite3
import functools

def log_queries(func):
    def wrapper(*args, **kwargs):
        print(f"Query: {kwargs['query']}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        yield result
    cursor.close()
    conn.close()

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
try:
    for user in users:
        print(user)
except BrokenPipeError:
    pass
except Exception as e:
    print(f"Error: {e}")
