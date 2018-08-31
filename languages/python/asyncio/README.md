# [AsyncIO](https://www.youtube.com/channel/UCwFl9Y49sWChrddQTD9QhRA/videos)
AsyncIO is, as it gives away, for executing multiple IO-bound tasks in the one main thread, asynchronously for the best  performace.
Compared to the traditional multiple threading model, IO-bound tasks can be handled efficiently enough on one main thread iif it's asynchronous.
I wouldn't use this model for multiple CPU-bound tasks. In that sense, it seems the philosophy of nodejs is similar to python's asyncio.

## Executing 10 IO-bound (simulated) tasks via asyncio. It tooks `max(timeit(task) for task in tasks)`, not `sum(timeit(task) for task in tasks)`
```
$ python3.6 example2.py
process id 2 is completed after 0 seconds
process id 3 is completed after 0 seconds
process id 6 is completed after 0 seconds
process id 1 is completed after 2 seconds
process id 7 is completed after 2 seconds
process id 8 is completed after 2 seconds
process id 0 is completed after 3 seconds
process id 4 is completed after 3 seconds
process id 5 is completed after 3 seconds
process id 9 is completed after 4 seconds
I am done in async def main!
I ran main until complete
```
