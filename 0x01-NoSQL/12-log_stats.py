#!/usr/bin/env python3
""" 12-main """
import bson


with open('dump/logs/nginx.bson', 'rb') as f:
    data = bson.decode_all(f.read())
f.close()
method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
count = len(data)
get = len([x for x in data if x['method'] == "GET"])
status = len([x for x in data if x['path'] == "/status"])

method_count = {}
for met in method:
    method_count[met] = len([x for x in data if x['method'] == met])

print(f"{count} logs")
print("Methods:")

for me in method_count.keys():
    print(f"  method {me}: {method_count[me]}")
print(f"{status} status check")

