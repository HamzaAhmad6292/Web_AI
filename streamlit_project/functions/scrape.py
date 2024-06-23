import requests
from langchain_community.document_loaders import WebBaseLoader

def scrape_website(url):
    try:
        # Send a GET request to the URL

        loader = WebBaseLoader(url)
        data = loader.load()
        
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None