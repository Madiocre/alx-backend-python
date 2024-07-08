#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Writes multiple corotine delays concurrently """
    lis_current = [task_wait_random(max_delay) for _ in range(n)]
    lis_fin = asyncio.as_completed(lis_current)
    delays = [await fin for fin in lis_fin]
    return delays
