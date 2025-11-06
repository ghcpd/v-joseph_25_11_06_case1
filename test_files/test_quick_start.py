import asyncio
from datasync import fetch_remote

async def main():
    data = await fetch_remote('/data/users')
    print('DATA:', data)

if __name__ == '__main__':
    asyncio.run(main())
