
numbers = [1,2,3]
#List Comprehension:  newList = [new_item for item in list]
newNumbers = [n + 1 for n in numbers]
print(newNumbers)

name = "Pedro"

letterList = [letter for letter in name]
print(letterList)



doubleNumbers = [numbers * 2 for numbers in range(1,5)]
print(doubleNumbers)

#List Comprehension:  newList = [new_item for item in list if test]
names = ["Pedro", "Giovana","Samuel","Leticia"]
bigNames = [name.upper() for name in names if len(name) >= 7]
print(bigNames)

import random
#new_dict={new_key:new_value for item in list}
student_score = {student:random.randint(1,100) for student in names}
print(student_score)

#new_dict={new_key:new_value for (key,value) in dict.items()}
passed_students = {student:score for (student,score) in student_score.items() if score >=60}
print(passed_students)

import pandas
#{new_key:new_value for (index,row) in dataframe.iterrows()}
