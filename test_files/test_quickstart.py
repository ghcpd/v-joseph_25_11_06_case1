# Quick Start snippet from README
from datasync import fetch_remote

if __name__ == '__main__':
    data = fetch_remote("/data/users")
    print(data)
