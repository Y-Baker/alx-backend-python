#!/usr/bin/env python3
"""
use a generator to compute a memory-efficient aggregate function i.e average age for a large dataset
"""
seed = __import__('seed')

def stream_user_ages():
    """
    yields user ages one by one.
    """
    connection = seed.connect_to_prodev()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT age FROM users")
        for row in cursor.fetchall():
            yield row['age']
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

def get_avg_age():
    """
    calculate the average age without loading the entire dataset into memory
    """

    count = 0
    summ = 0
    for age in stream_user_ages():
        count += 1
        summ += age

    if count == 0:
        print("No data found")
        return

    print(f"Average age of users: {summ / count}")


if __name__ == "__main__":
    get_avg_age()
