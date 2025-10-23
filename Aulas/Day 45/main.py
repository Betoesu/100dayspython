from bs4 import BeautifulSoup
import requests

endpoint = "https://news.ycombinator.com/news"
response = requests.get(endpoint)


yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")