#!/usr/bin/env python3
"""async comprehension"""
import asyncio
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_generator() -> Generator[float, None, None]:
    """doc
    """
    return [vaule async for value in async_generator()]
