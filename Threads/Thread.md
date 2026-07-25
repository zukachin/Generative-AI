# What is a thread?
- Is like where multiple workers working simultaneously on different tasks

# Three patterns
1. Function-based threading

```python
import threading
def worker(name):
    print(f"Task {name}")
thread = threading.Thread(target=worker, args=("A",)) # this part where thread gets created
thread.start() # wakes up and tell hey start the work
thread.join() # Wait for thread to finish - like wait until i finish it

```
2. Class-based threading
```python
class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print(f"Task {self.name}")

thread = Worker("A")
thread.start()
```
3. ThreadPoolExecutor (recommended)
```python
from concurrent.futures import ThreadPoolExecutor

def fetch_url(url):
    return requests.get(url).text

with ThreadPoolExecutor(max_workers=5) as executor:
    # Automatically manages threads
    results = executor.map(fetch_url, urls)
    for result in results:
        print(result)
```
# Problem arises 
1. Race condition - where threads modify same data at the same time
2. Deadlock - threads wait forever

# Solution:
- use Lock - Until one finishes and other wait like a bathroom stall, if a door is locked the other wait until it gets released.

# To Log threads
1. use python logging
2. use print statements
3. use threading.current_thread() - Get info about current thread (name, ID, status).
    - current_thread().name → Thread's custom name (or "Thread-1", "Thread-2")
    - current_thread().ident → Unique thread ID (big number)
    - current_thread().is_alive() → True if running, False if done