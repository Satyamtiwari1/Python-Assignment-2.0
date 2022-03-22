# importing the libraries
from bs4 import BeautifulSoup
import requests

url="https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, 'html.parser')
# print the parsed data of html
print(soup.text) 