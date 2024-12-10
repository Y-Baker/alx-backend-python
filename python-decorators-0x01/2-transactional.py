#!/usr/bin/env python3
"""
create a decorator that manages database transactions by automatically committing or rolling back changes
"""

import sqlite3
import functools

with_db_connection = __import__('1-with_db_connection').with_db_connection

def transactional(func):
    """
    ensures a function running a database operation is wrapped inside a transaction.
    If the function raises an error, rollback;
    otherwise commit the transaction
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        if not conn:
            raise Exception('Connection Can not found')
        try:
            re = func(conn, *args, **kwargs)
            conn.commit()
            return re
        except Exception as e:
            conn.rollback()
            raise e
    return wrapper

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    users = cursor.fetchall()
    print(users)

    cursor.execute("UPDATE users SET email = ? WHERE user_id = ?", (new_email, str(user_id)))
 
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    users = cursor.fetchall()
    print(users)

if __name__ == '__main__':
    update_user_email(user_id="70cef897-5095-44dd-ba79-a9efbf1f82a5", new_email='Crawford_Cartwright@hotmail.com')