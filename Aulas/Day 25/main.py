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
