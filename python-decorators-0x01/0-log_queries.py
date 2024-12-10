#!/usr/bin/env python3

import sqlite3
import functools
from datetime import datetime

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or args[0]
        timeNow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"At {timeNow} - Query: {query} running...")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    """Fetch all users from the database"""
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
