#!/usr/bin/env python3
# since I'm using 3.6, not 3.7 ...
# reference: https://www.youtube.com/watch?v=tmMqdrEzVRI&t=12s
# Jin's comment:
# async loop helps us to write coroutines that work concurrently
# in a main thread. To ensure that every coroutine co-work together
# we need to use asyncio.sleep inside each coroutine so the others
# may have a time slot to be executed.
# We should note that this is concurrent, not of parallelism.

import asyncio
import time

async def taskA():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)

async def taskB():
    start_time = time.time()
    while True:
        dur = int(time.time() - start_time)
        if dur % 3 == 0:
            print (f"{dur} seconds has passed")
        # await can't block the main thread here
        # it must be working like a generator:
        # - it surrender it's execution 
        # - yet, it should be resumable later
        #   hence a iterableWrapper in the event loop ...?
        #   and maybe in a timer-like form in a heap data structure
        await asyncio.sleep(1)

async def main():
    ta = asyncio.ensure_future(taskA())
    tb = asyncio.ensure_future(taskB())
    # this await seems a bit different from the one from asyncio.sleep,
    # at a first glance, because await here for 'gather' seems waiting
    # for those tasks to be finished unlike 'sleep'.
    # But I guess the asyncio.gather register callback_on_done for future
    # and then it counts if all the tasks are gathered.
    # So, asyncio.gather also wouldn't block the main thread here, but
    # it only check, in the event loop, if the loop can now be breakable
    # at the moment. 'Await' here is a symantic marker for the users
    # to be able to think this concurrent programming as a imperative way.
    await asyncio.gather(ta, tb)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

