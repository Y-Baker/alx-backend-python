#!/usr/bin/env python3
"""
Setup the SQLite3 database connection and seed data
"""

from sqlite3 import connect

import uuid
import csv

def connect_db():
    """Connect to the SQLite3 database"""
    return connect('users.db')

def create_table(connection):
    """Create Table `users`"""
    try:
        p = connection.cursor()
        p.execute("""CREATE TABLE IF NOT EXISTS users (
                      user_id TEXT PRIMARY KEY,
                      name TEXT NOT NULL,
                      email TEXT NOT NULL,
                      age INTEGER NOT NULL)""")
    except Exception as e:
        print(f"Error: {e}")
        raise e

def __read_data(filepath):
    """Read data from a file"""
    with open(filepath, 'r') as f:
        data = csv.DictReader(f)
        for row in data:
            yield row

def insert_data(connection, data):
    """Insert data into the table `users`"""
    try:
        p = connection.cursor()
        for row in __read_data(data):
            p.execute("""INSERT INTO users (user_id, name, email, age) VALUES (?, ?, ?, ?)""", (str(uuid.uuid4()), row['name'], row['email'], row['age']))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
        raise e

def setup():
    """Setup the database connection and seed data"""
    try:
        connection = connect_db()
        create_table(connection)
        insert_data(connection, 'user_data.csv')
    except Exception as e:
        pass
    finally:
        connection.close()

if __name__ == '__main__':
    setup()
