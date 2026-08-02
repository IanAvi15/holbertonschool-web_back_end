# Async Python: Asyncio, Coroutines, and Concurrency

This project introduces asynchronous programming in Python using the asyncio library. You will learn how async and await work, how to run coroutines concurrently, how to create and manage tasks, and how randomness can be incorporated into asynchronous workflows. By the end of this project, you should be able to explain these concepts confidently without relying on external references.

# Learning Objectives

Async and Await Syntax
Understand the purpose of async def and how coroutines differ from regular functions

Learn how await suspends execution until an awaited coroutine or task completes

Recognize when asynchronous code is beneficial compared to synchronous execution

Executing Async Programs with asyncio
Use asyncio.run() to execute top-level coroutines

Understand the event loop and how it schedules asynchronous operations

Learn how asynchronous execution avoids blocking the program

Running Concurrent Coroutines
Execute multiple coroutines at the same time using asyncio.gather()

Understand concurrency vs parallelism in Python’s async model

Learn how concurrent coroutines improve performance for I/O-bound tasks

Creating asyncio Tasks
Use asyncio.create_task() to schedule coroutines concurrently

Manage tasks, await their results, and understand task lifecycle

Learn how tasks allow background execution while other code continues running

Using the random Module
Generate random values inside asynchronous functions

Combine randomness with async delays or operations

Understand how random behavior interacts with concurrency

# Requirements

Environment
Ubuntu 20.04 LTS

Python 3.8

Allowed editors: vi, vim, emacs

Code Standards
All files must be executable

First line must be: #!/usr/bin/env python3

Code must follow pycodestyle 2.5.x

All modules and functions must include full documentation strings

All functions and coroutines must be type‑annotated using Python 3.8‑compatible types

File lengths will be checked using wc

# Goal of the Project

The purpose of this project is to help you understand how asynchronous programming works in Python. You will learn how to write non‑blocking code, run multiple operations concurrently, and use asyncio effectively to build efficient asynchronous workflows.

# Author

Ian Aviles