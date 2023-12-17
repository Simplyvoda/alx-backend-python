#!/usr/bin/env python3
'''
This module imports a function
Contains a function that takes 2 integers
and measures the total execution time
returning total_time / n a float
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time (n: int, max_delay: int) -> float :
  '''
  Computes the runtime for wait_n
  '''
  start_time = time.time()
  asyncio.run(wait_n(n, max_delay))
  end_time = time.time()
  return (end_time - start_time)/n