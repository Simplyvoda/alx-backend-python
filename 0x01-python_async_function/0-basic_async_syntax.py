#!/usr/bin/env python3
'''
This module contains an async coroutine that takes
an integer argument and waits for random delay
then eventually returns the delay
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
  '''
  This function uses the random module
  to get a random number, delays execution
  by that number and then returns the number
  '''
  random_delay = random.uniform(0, max_delay)
  await asyncio.sleep(random_delay)
  return random_delay