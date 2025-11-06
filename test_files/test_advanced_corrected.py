from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from datasync import DataSync
import asyncio

if __name__ == '__main__':
    sync = DataSync("http://localhost:8000")
    mapping = {
        "data/users": "output/users.json",
        "data/info": "output/info.json",
    }
    res = asyncio.run(sync.sync_all(mapping))
    print(res)
