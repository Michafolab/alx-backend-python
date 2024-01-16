#!/usr/bin/env python3
"""async comprehension"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_generator() -> List[float]:
    """doc
    """
    return [vaule async for value in async_generator()]
