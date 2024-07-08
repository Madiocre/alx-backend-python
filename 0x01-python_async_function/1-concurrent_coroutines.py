#!/usr/bin/env python3
""" Multiple concurrent corotines """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Writes multiple corotine delays concurrently """
    lis_current = [wait_random(max_delay) for _ in range(n)]
    lis_fin = asyncio.as_completed(lis_current)
    delays = [await fin for fin in lis_fin]
    return delays
