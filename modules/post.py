import requests
from bs4 import BeautifulSoup

def extract_info(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "No Title"
        description = soup.find("meta", property="og:description")
        desc = description["content"] if description else "No description found."
        return f"**{title}**\n\n{desc}\n\nLink: {url}"
    except Exception as e:
        return f"Error extracting content: {e}"
