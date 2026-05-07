import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(resp.status_code)
print(resp.json())