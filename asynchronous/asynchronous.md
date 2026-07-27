# what is actually asynchronous means in simple words?
- Is basically a task would wait for its I/O and let other tasks to work.
- Async waits.

# Three basic concepts to know
1. coroutines - async def
- Coroutines refers to a specialized function that can pause its execution and resume later.
```python
    async def fetch_data(url):
        data = await requests.get(url)
```
- This "async" is a keyword to make the function indicating this can pause and resume.

2. Pause execution - await
``` python
    result = await fetch_data(url)
```
- Here "await" keyword pauses the function until the operation is over.
- Only inside the async function this keyword works.
- so, other coroutines works while you wait.

3. Execute - asynchio.run()
``` python
asyncio.run(fetch_data(url))
```
- Use this at the top level to run async code
- This starts the event loop.

# Example: Fetching mutliple urls concurrently using asyncio and aiohttp
 ```python
import asyncio
import aiohttp

async def fetch_url(session,url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
            'https://www.example.com',
            'https://www.python.org',
            'https://www.asyncio.org'
        ]
        results = await asyncio.gather(*(fetch_url(session,url) for url in urls))
        return results
asyncio.run(main())

```
# Key functions

1. asyncio.gather() - Run multiple coroutines,wait for all
2. asyncio.create_task() - Schedule a coroutine in the background
3. asyncio.sleep() - Non-blocking pause (Not time.sleep)
4. asyncio.wait() - Wait for first/all tasks to complete



# Most frequently used function
1. asyncio.gather():
    All fuctions(tasks) will get started until all gets completed then only at finally it shows us final output.
2. async def:
    Indicating a function to run as asynchronously.
3. await:
    Pauses the function to get its input letting other functions to run in that time.
4. asyncio.run():
    Starting point for the async to run.
5. asyncio.create_task():
    Function gets started in the background so it can run other functions concurrently.
6. asyncio.sleep():
    Blocks the current function but letting all other function keep running.
7. asyncio.wait_for():
    cancels the function when time exceeds.
8. asyncio.Semaphore:
    sets limit for the async function so that it runs in a batch waits until the task gets completed once done another tasks jump in.
9. asyncio.Lock:
    Resources get locked for others until one gets finish the task.
10. asyncio.Event:
    Function that signals to a other function. no data is been passed. only signals is passed.
11. asyncio.Queue:
    Functions produces and functions consumes. Data is transferred.
12. asyncio.as_completed():
    Returns the results once each task gets over.
13. asyncio.wait():
    Waits for all the async tasks to complete but gives us more control than the gather() it gives like done, pending status. But gather() only gives completed status.
14. asyncio.to_thread():
    Puts your particular function into a separate thread - to run synchronously and letting others to run asynchronously. 


