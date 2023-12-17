#!/usr/bin/env python3
'''
Module imports task_wait_random
and runs the containing function
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
  '''
  This function executes task_wait_random n times
  '''
  delayList = []
  for _ in range(n):
    response = await task_wait_random(max_delay)
    delayList.append(response)
  return sorted(delayList)