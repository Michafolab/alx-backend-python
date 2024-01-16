#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """doc
    """
    start = time.pref_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.pref_counter() - start
    return end / n
