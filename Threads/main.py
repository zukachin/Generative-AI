from concurrent.futures import ThreadPoolExecutor
import threading
import logging
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(threadName)s | %(levelname)s | %(message)s"
)

def worker(n):
    logging.info(f"Worker {n} starting")

    time.sleep(2)

    logging.info(f"ID of worker thread: {threading.current_thread().ident}")
    logging.info(f"Alive threads: {threading.active_count()}")

    logging.info(f"Worker {n} done")
    return n * 2


with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(worker, range(3)))

logging.info(f"Results: {results}")