#!/usr/bin/env python3
"""
create a generator that streams rows from an SQL database one by one.
"""

from mysql.connector import connect

def stream_users_in_batches(batch_size):
    """fetch and process data in batches from the users database"""
    connection = connect(host='localhost', user='youse', password='root', database='ALX_prodev')

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM users LIMIT {batch_size};")
            while True:
                batch = cursor.fetchone()
                if not batch:
                    break
                yield batch
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()


def batch_processing(batch_size):
    """process the data stream from the database processes each batch to filter users over the age of `25`"""
    for batch in stream_users_in_batches(batch_size):
        if batch['age'] > 25:
            yield batch
