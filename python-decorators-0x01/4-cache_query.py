#!/usr/bin/env python3
"""
create a decorator that caches the results of a database queries inorder to avoid redundant calls
"""

import time
import sqlite3 
import functools

with_db_connection = __import__('1-with_db_connection').with_db_connection

query_cache = {}

def cache_query(func):
    """caches query results based on the SQL query string"""

    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        if not conn:
            raise Exception("Connection can't found")
        
        query = kwargs.get('query') or (args[0] if len(args) > 0 else None)
        if not query:
            raise Exception("Query Not Found")
        
        if query in query_cache:
            print("Query Cashe Found")
            return query_cache[query]
        re = func(conn, *args, **kwargs)
        query_cache[query] = re
        return re
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")