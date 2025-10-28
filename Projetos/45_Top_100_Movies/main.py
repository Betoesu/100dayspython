from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")


#Primeiro achamos tudo que tem tag h2 e no for loop filtramos oq também tem strong, que no nosso caso são os filmes
h2 = soup.find_all("h2")

top_100_movies_desc = []
for h2_tag in h2:
    strong_tag = h2_tag.find("strong")

    if strong_tag:  # Confere que não a None type 
        text = strong_tag.getText()
        top_100_movies_desc.append(text)

top_100_movies_crec = top_100_movies_desc[::-1] #Inverte a ordem da lista

for movie in top_100_movies_crec:
    #Método de tirar o ano do filme
    movie_list = movie.split()
    movie_list.pop()
    movie_name = ' '.join(movie_list)

    with open("./Projetos/45_Top_100_Movies/Top_100_Movies.txt", "a", encoding="utf-8") as file:
        file.writelines(f"{movie_name}\n") 