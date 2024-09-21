import requests

url = 'http://dummyjson.com/products'
responce = requests.get(url)
if responce.status_code == 200:
    data = responce.json
    for x in data["product"]:
        name = x["title"]
        print(name)