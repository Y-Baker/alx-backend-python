#!/usr/bin/env python3
"""
create a decorator that retries database operations if they fail due to transient errors
"""

import time
import sqlite3 
import functools

with_db_connection = __import__('1-with_db_connection').with_db_connection


def retry_on_failure(retries=3, delay=0.5):
    """decorator that retries the function a certain number of times if it raises an exception
    
    Keyword arguments:
    retries -- number of retries default 3
    delay   -- time delay between retries
    Return: wrapper function
    """
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(conn, *args, **kwargs):
            if not conn:
                raise Exception("Connection not found")
            for attempt in range(retries):
                try:
                    result = func(conn, *args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Error {e}, Attempt {attempt + 1} failed...Try Again in {delay} seconds.")
                    time.sleep(delay)
                    if attempt == retries - 1:
                        raise e
        return wrapper
    return decorator

    

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


if __name__ == '__main__':
    users = fetch_users_with_retry()
    print(users)
