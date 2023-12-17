#!/usr/bin/env python3
'''
Module imports wait_random
and runs the containing function
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    This function executes wait_random n times
    '''
    delayList = []
    for _ in range(n):
        response = await wait_random(max_delay)
        delayList.append(response)
    return sorted(delayList)