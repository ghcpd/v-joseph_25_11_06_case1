from datasync import DataSync

sync = DataSync("https://api.example.com")

result = sync.sync_all({
    "data/users": "output/users.json",
    "data/info": "output/info.json"
})
print(result)
