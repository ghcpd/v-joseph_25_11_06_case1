import asyncio
from datasync import DataSync

async def main():
    ds = DataSync("https://httpbin.org")
    data = await ds.fetch_remote("/get")
    print(data[:60])

if __name__ == '__main__':
    asyncio.run(main())
