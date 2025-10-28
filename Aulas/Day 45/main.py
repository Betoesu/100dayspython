from bs4 import BeautifulSoup
import requests

endpoint = "https://news.ycombinator.com/news"
response = requests.get(endpoint)
yc_webpage = response.text
print(yc_webpage)

soup = BeautifulSoup(yc_webpage,"html.parser")


article = soup.find_all("span", class_="titleline")


article_texts = []
article_links = []
for article_tag in article:
    a_tag = article_tag.find("a")
    if a_tag:
        text = a_tag.getText()
        article_texts.append(text)
        link = a_tag.get("href")
        article_links.append(link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]


# print(article_texts)
# print(article_links)
# print(article_upvotes)

higher_upvote = max(article_upvotes)
print(higher_upvote)

index_higher_upvote = article_upvotes.index(higher_upvote)
print(F"{index_higher_upvote}\n")


print(article_texts[index_higher_upvote])
print(article_links[index_higher_upvote])
print(article_upvotes[index_higher_upvote])
