#!/usr/bin/env python3
"""
create a decorator that automatically handles opening and closing database connections
"""

import sqlite3 
import functools

connector = __import__('seed').connect_db

def with_db_connection(func):
    """opens a database connection, passes it to the function and closes it afterword""" 
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = kwargs.get('conn') or (args[0] if len(args) > 0 else None)
        if not conn:
            conn = connector()
        re = func(conn, *args, **kwargs)
        conn.close()
        return re
    return wrapper



@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)) 
    return cursor.fetchone() 

#### Fetch user by ID with automatic connection handling
if __name__ == '__main__':
    user = get_user_by_id(user_id="70cef897-5095-44dd-ba79-a9efbf1f82a5")
    print(user)
