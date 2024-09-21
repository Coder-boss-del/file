import requests
from bs4 import BeautifulSoup

def scrape_movies(url):
    # Send a GET request to the page
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Define a list to store movie details
    movies = []

    # Adjust the selector based on the actual HTML structure of the website
    for item in soup.select('.movie-item'):
        title = item.select_one('.movie-title').get_text(strip=True)  # Adjust selector
        link = item.select_one('a')['href']  # Adjust selector
        description = item.select_one('.movie-description').get_text(strip=True)  # Adjust selector

        movies.append({
            'Title': title,
            'Description': description,
            'Link': link
        })

    return movies

def main():
    base_url = 'https://nkiri.com/'  # Replace with the actual URL
    movies = scrape_movies(base_url)

    # Print the scraped data
    for movie in movies:
        print(f"Title: {movie['Title']}")
        print(f"Description: {movie['Description']}")
        print(f"Link: {movie['Link']}")
        print('---')

if __name__ == "__main__":
    main()
