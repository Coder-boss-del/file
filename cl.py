import requests
from bs4 import BeautifulSoup

# 117

base_url = "https://www.arise.tv/category/sports/page/"

n = range(117)
for numb in n:
    url = f"{base_url}{numb}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for data in soup.find_all('article'):
        title = data.find('h3').text.strip()
        print(title)

        url = data.find("a")
        if url:
            link = url.get('href')
            print(link)
        print("\n")

        image = data.find("img")
        if image:
            img = image.get('src')
            print(img)
        print("\n")