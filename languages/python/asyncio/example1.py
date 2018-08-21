#!/usr/bin/env python3

import asyncio

async def my_coroutine():
    print("jinsung is here")

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_coroutine())
    loop.close()

main()
