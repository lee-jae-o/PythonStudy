import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        first_paragraph = soup.find('p').text
        return first_paragraph
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)
        return None

def main():
    wikipedia_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    content = scrape_wikipedia(wikipedia_url)

    if content:
        print("First paragraph from Wikipedia:")
        print(content)

if __name__ == "__main__":
    main()