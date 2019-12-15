#!/usr/bin/python3
from concurrent.futures import ThreadPoolExecutor
import os


pool = ThreadPoolExecutor(max_workers = 5)
while True:
    try:
        command = input()
        pool.submit(os.system, command)
    except EOFError:
        break
