#!/usr/bin/env python3
"""
create a reusable context manager that takes a query as input and executes it, managing both connection and the query execution
"""

open_connection = __import__('seed').connect_db

class ExecuteQuery:
    """
    custom context manager that takes the query and parameters to execute
    and return the result of the query
    """
    def __init__(self, query, parameters=()):
        self.connection = None
        self.query = query
        self.parameters = parameters
    
    def __enter__(self):
        self.connection = open_connection()
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(self.query, self.parameters)
            return self.cursor
        except Exception as e:
            print(f"Error: {e}")
            raise e
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()

if __name__ == '__main__':
    query = "SELECT * FROM users WHERE age > ?"
    with ExecuteQuery(query, (25,)) as cursor:
        for row in cursor.fetchall():
            print(row)