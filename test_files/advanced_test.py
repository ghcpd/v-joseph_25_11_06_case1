import asyncio
from datasync import DataSync

async def main():
    ds = DataSync("https://httpbin.org")
    result = await ds.sync_all({
        "get": "output/users.json",
        "/get?show=info": "output/info.json"
    })
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
