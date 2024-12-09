#!/usr/bin/env python3
"""
Setup the MySQL database connection
"""

from mysql.connector import connect
import uuid
import csv

def connect_db():
    """Connect to the MySQL database"""
    return connect(host='localhost', user='yousef', password='root')

def create_database(connection):
    """Create Database `ALX_prodev`"""
    try:
        with connection.cursor() as p:
            p.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    except Exception as e:
        print(f"Error: {e}")

def connect_to_prodev():
    """Connect to the MySQL database `ALX_prodev`"""
    return connect(host='localhost', user='yousef', password='root', database='ALX_prodev')

def create_table(connection):
    """Create Table `users`"""
    try:
        with connection.cursor() as p:
            p.execute("""CREATE TABLE IF NOT EXISTS users (
                      user_id VARCHAR(64) PRIMARY KEY,
                      name VARCHAR(255) NOT NULL,
                      email VARCHAR(255) NOT NULL,
                      age INT NOT NULL)""")
    except Exception as e:
        print(f"Error: {e}")

def __read_data(filepath):
    """Read data from a file"""
    with open(filepath, 'r') as f:
        data = csv.DictReader(f)
        for row in data:
            yield row


def insert_data(connection, data):
    """Insert data into the table `users`"""
    try:
        with connection.cursor() as p:
            for row in __read_data(data):
                p.execute("""INSERT INTO users (user_id, name, email, age) VALUES (%s, %s, %s, %s)""", (str(uuid.uuid4()), row['name'], row['email'], row['age']))
            connection.commit()
    except Exception as e:
        print(f"Error: {e}")
