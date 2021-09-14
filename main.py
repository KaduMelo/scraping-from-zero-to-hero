import requests
from bs4 import BeautifulSoup

response = requests.get("https://zenrows.com")
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.title.string) # Web Data Automation Made Easy - ZenRows