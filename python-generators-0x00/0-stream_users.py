#!/usr/bin/env python3
"""
create a generator that streams rows from an SQL database one by one.
"""

from mysql.connector import connect

def stream_users():
    """uses a generator to fetch rows one by one from the users"""
    connection = connect(host='localhost', user='yousef', password='root', database='ALX_prodev')
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users;")
            for row in cursor:
                yield row
    finally:
        connection.close()

