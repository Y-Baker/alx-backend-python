#!/usr/bin/env python3
"""
Run multiple database queries concurrently using asyncio.gather
"""

import asyncio
import aiosqlite
from aiosqlite import connect as aconnect

async def async_fetch_users():
    """
    Fetch all users from the database
    """
    users = []
    async with aconnect("users.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            async for row in cursor:
                print(f"1- {row}")
                users.append(row)
    return users



async def async_fetch_older_users():
    """
    Fetch users older than 40 from the database
    """
    users = []
    async with aconnect("users.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            async for row in cursor:
                print(f"2- {row}")
                users.append(row)
    return users

async def fetch_concurrently():
    all_users, older_users = await asyncio.gather(async_fetch_users(), async_fetch_older_users())

if __name__ == '__main__':
    asyncio.run(fetch_concurrently())
