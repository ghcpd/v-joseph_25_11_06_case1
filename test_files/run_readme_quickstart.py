"""Run README Quick Start example exactly as written to reproduce issues."""
from datasync import fetch_remote

data = fetch_remote("/data/users")
print(data)
