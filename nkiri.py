import requests
from bs4 import BeautifulSoup


url = 'https://nkiri.com/'  


response = requests.get(url)
response.raise_for_status() 

# Parse the page content
soup = BeautifulSoup(response.text, 'html.parser')

# Define the data to scrape
data = []
for item in soup.select('.item-class'):  # Replace '.item-class' with the actual class or HTML structure
    title = item.select_one('.title-class').get_text(strip=True)  # Adjust selectors
    description = item.select_one('.description-class').get_text(strip=True)  # Adjust selectors
    link = item.select_one('a')['href']  # Adjust selectors

    data.append({
        'Title': title,
        'Description': description,
        'Link': link
    })

# Define the text file path
text_file_path = 'scraped_data.txt'

# Write data to a plain text file
with open(text_file_path, mode='w', encoding='utf-8') as file:
    for entry in data:
        file.write(f"Title: {entry['Title']}\n")
        file.write(f"Description: {entry['Description']}\n")
        file.write(f"Link: {entry['Link']}\n")
        file.write('---\n')

print(f"Scraping completed and data saved to '{text_file_path}'.")


import requests
from bs4 import BeautifulSoup


url = 'https://nkiri.com/movies' 


response = requests.get(url)
response.raise_for_status() 

# Parse the page content
soup = BeautifulSoup(response.text, 'html.parser')

movie_containers = soup.select('.movie-item') 
for container in movie_containers:
    title = container.select_one('.movie-title').get_text(strip=True) 
    link = container.select_one('a.download-link')['href']  

    print(f"Movie Title: {title}")
    print(f"Download Link: {link}")
    print('---')
