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
