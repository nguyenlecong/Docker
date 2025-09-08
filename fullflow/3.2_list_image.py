import requests

username = "nguyenlc41"
url = f"https://hub.docker.com/v2/repositories/{username}/?page_size=100"

resp = requests.get(url).json()
for repo in resp["results"]:
    print(repo["name"])
