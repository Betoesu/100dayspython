#with open("./Aulas/Day 25/weather_data.csv") as weather_data:
#    datas = weather_data.readlines()
#for data in datas:
#    data.replace("\n", "")
#    print(data)

# import csv

# with open("./Aulas/Day 25/weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)

#     num_rows = 0
#     temperatures = []
#     for row in data:
#         num_rows += 1 
#         if num_rows != 1:
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("./Aulas/Day 25/weather_data.csv")
print(data["temp"])

dataDict = data.to_dict()
print(dataDict)

tempList = data["temp"].to_list()
print(tempList)

media = sum(tempList)/len(tempList) 
print(round(media,2))

#^ Maneira de se fazer usando o própio python
#|
#|
#v Maneira de fazer usando .mean() (Faz a media)
print(data["temp"].mean())

highestTemperature = data["temp"].max()
print(highestTemperature)

#Pegar informacoes nas colunas
print(data["condition"])
print(data.condition) 

#Pegar informacoes nas linhas
print(data[data.day == "Monday"])

#Informação de toda a linha do dia mais quente
temperature = data.temp
print(data[temperature == highestTemperature])

monday = data[data.day == "Monday"]
print(monday.condition)

mondayTemperatureCelsius = monday.temp[0]
mondayTemperatureFahrenheit = (mondayTemperatureCelsius * 9/5) + 32
print(mondayTemperatureFahrenheit)

#Create a dataframe from scratch
dataDict = {
    "students": ["Amy", "James","Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(dataDict)
data.to_csv("./Projetos/25_Starting_Pandas/new_data.csv")


import pandas 

#começo atribuindo o conteudo do documento para a variavel data
data = pandas.read_csv("./Projetos/25_Squirrel_Data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250807.csv ")
dataPFC = data["Primary Fur Color"] #aqui especifico e recebo informações somente da coluna Primary Fur Color

#Começo meu contador
graySquirrels = 0
cinammonSquirrels = 0
blackSquirrels = 0

#Aqui faço um loop para contar cada vez que aparecer o nome Gray, Cinammon ou Black
for squirrel in dataPFC:
    if squirrel == "Gray":
        graySquirrels += 1
    elif squirrel == "Cinnamon":
        cinammonSquirrels += 1
    elif squirrel == "Black":
        blackSquirrels += 1

#Aqui eu crio um dicionario para facilitar a criação do arquivo csv
squirrelCount = {"Fur Color": ["Gray", "Cinammon", "Black"],
                 "Count": [graySquirrels, cinammonSquirrels, blackSquirrels]}

#Crio um quadro de dados
data = pandas.DataFrame(squirrelCount)
#E transformo ele em csv e crio o arquivo
data.to_csv("./Projetos/25_Squirrel_Data/squirrel_count.csv ")  


