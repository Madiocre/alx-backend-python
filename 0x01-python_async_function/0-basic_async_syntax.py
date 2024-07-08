#!/usr/bin/env python3
""" Using corotines async and await to make a delay function """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Function to create a delay between 0
    and a number inputed by user
    """
    rand_delay = random.uniform(0, max_delay)
    await asyncio.sleep(rand_delay)
    return rand_delay
