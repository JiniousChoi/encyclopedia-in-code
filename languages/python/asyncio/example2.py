#!/usr/bin/env python3

import asyncio
import random

async def my_coroutine(_id):
    process_time = random.randint(0, 5)
    await asyncio.sleep(process_time)
    print("process id {} is completed after {} seconds".format(_id, process_time))

async def main():
    tasks = []
    for _id in range(10):
        tasks.append(asyncio.ensure_future(my_coroutine(_id)))
        
    await asyncio.gather(*tasks)
    print("I am done in async def main!")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("I ran main until complete")
loop.close()
