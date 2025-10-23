from bs4 import BeautifulSoup

with open("./Aulas/Day 45/website.html") as html_file:
    contents = html_file.read()
   
#Guarda o código HTML
soup = BeautifulSoup(contents, "html.parser")

#Retorna a string dentro da tag title
# print(soup.title.string)

#Organiza o código HTML
# print(soup.prettify())


#Retorna uma lista de todos as tags a
all_a_tags = soup.find_all(name="a")
# print(all_a_tags)

#Pegar tudo dentro de todas as a tags
for tag in all_a_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass


heading = soup.find(name="h1",id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

print(soup.select_one(selector="p a"))

print(soup.select(".heading"))