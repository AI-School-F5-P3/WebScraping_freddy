import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_author_about(author_url):
    response = requests.get("https://quotes.toscrape.com" + author_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    about = soup.find('div', class_='author-description').text.strip()
    return about

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quotes = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        author_url = quote.find('a')['href']
        about = get_author_about(author_url)
        quotes.append({'text': text, 'author': author, 'tags': tags, 'about': about})
    
    return pd.DataFrame(quotes)

if __name__ == "__main__":
    df = scrape_quotes()
    print(df)