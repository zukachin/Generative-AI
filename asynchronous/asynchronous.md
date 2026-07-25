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