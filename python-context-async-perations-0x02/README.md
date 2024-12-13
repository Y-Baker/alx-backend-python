## Context Managers and Asynchronous

### Key Highlights

1. Task 0: custom class based context manager for Database connection

- Write a class custom context manager DatabaseConnection using the __enter__ and the __exit__ methods.
- Use the context manager with the `with` statement to be able to perform the query SELECT * FROM users. Print the results from the query.

2. Task 1: Reusable Query Context Manager

- Implement a class based custom context manager ExecuteQuery that takes the query: ”SELECT * FROM users WHERE age > ?” and the parameter 25 and returns the result of the query.
- Ensure to use the__enter__() and the __exit__() methods.

3. Task 2: Concurrent Asynchronous Database Queries

- Use the aiosqlite library to interact with SQLite asynchronously. To learn more about it, click here.
- Write two asynchronous functions: async_fetch_users() and async_fetch_older_users() that fetches all users and users older than 40 respectively.
- Use the asyncio.gather() to execute both queries concurrently.
- Use asyncio.run(fetch_concurrently()) to run the concurrent fetch.


## Authors :black_nib:

* __Yousef Bakier__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br />
 &nbsp;&nbsp;[<img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github">](https://github.com/Y-Baker)