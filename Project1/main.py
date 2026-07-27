import requests
import sys
import asyncio
import aiohttp
import logging
# logging.basicConfig(level=logging.INFO)


urls = [
    "https://proof.ovh.net/files/10Mb.dat",
    "https://proof.ovh.net/files/100Mb.dat",
    "https://proof.ovh.net/files/1Gb.dat"
]


async def download_file_async(session, url, filename):
     last_logged = 0
     headers = {"User-Agent": "Mozilla/5.0"}
     logging.info(f"Starting download: {filename}")
     async with session.get(url, headers=headers) as response:
         total = int(response.headers.get('content-length', 0))
         with open(filename, "wb") as f:
             downloaded = 0
             async for chunk in response.content.iter_chunked(1024*1024):
                 f.write(chunk)
                 downloaded += len(chunk)
                 print(f"{filename}: received {len(chunk)} bytes")
                 percentage = (downloaded / total) * 100
                 if percentage >= last_logged + 10:
                    last_logged += 10
                    logging.info(f"{filename}: {last_logged}%")
             logging.info(f"{filename} Download completed")


async def download_file_async_v2(session, url, filename):
     last_logged = 0
     headers = {"User-Agent": "Mozilla/5.0"}
     async with session.get(url, headers=headers) as response:
         total = int(response.headers.get('content-length', 0))
         with open(filename, "wb") as f:
             downloaded = 0
             async for chunk in response.content.iter_chunked(1024*1024):
                 f.write(chunk)
                 downloaded += len(chunk)
                 print(f"{filename}: received {len(chunk)} bytes")
                 percentage = (downloaded / total) * 100
                 if percentage >= last_logged + 10:
                    last_logged += 10


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            download_file_async_v2(session, urls[0], "file1.bin"),
            download_file_async_v2(session, urls[1], "file2.bin"),
            download_file_async_v2(session, urls[2], "file3.bin")
        )

if __name__ == "__main__":
    asyncio.run(main())
   