import asyncio

# simple example: 3 tasks that take 1 second each to complete
async def task(name):
    print(f"Task {name} started")
    await asyncio.sleep(1)
    print(f"Task {name} completed")
    return f"Result of task {name}"

async def main():
    # run all 3 at the same time (takes 1 sec to complete, not 3 sec)
    results = await asyncio.gather(
        task("A"),
        task("B"),
        task("C")
    )
    print(results)

asyncio.run(main())