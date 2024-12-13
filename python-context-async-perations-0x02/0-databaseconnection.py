#!/usr/bin/env python3
"""
create a class based context manager to handle opening and closing database connections automatically
"""
open_connection = __import__('seed').connect_db

class DatabaseConnection:
    """
    Custom class to handle database connection
    """
    def __init__(self):
        """
        Constructor
        """
        self.connection = None

    def __enter__(self):
        """
        Method to open the connection
        """
        self.connection = open_connection()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Method to close the connection and handle exceptions
        """
        self.connection.close()

if __name__ == '__main__':
    with DatabaseConnection() as connection:
        try:
            curosr = connection.cursor()
            curosr.execute("SELECT * FROM users")
            for row in curosr.fetchall():
                print(row)
        except Exception as e:
            print(f"Error: {e}")
            raise e
