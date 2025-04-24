test_dictionary = {
    "bug": "An error",
    "function": "A piece of code that you can call over again"
}

print(test_dictionary["function"])

for key in test_dictionary:
    print(key)
    print(test_dictionary[key])



    student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for students in student_scores:
    if student_scores[students] >= 91 and student_scores[students] <= 100:
        student_scores[students] = "Outstanding"
        
    elif student_scores[students] >= 81 and student_scores[students] <= 90:
        student_scores[students] = "Exceeds Expectations"
        
    elif student_scores[students] >= 71 and student_scores[students] <= 80:
        student_scores[students] = "Acceptable"
        
    elif student_scores[students] <= 70:
        student_scores[students] = "Fail"

student_grades = student_scores

for student in student_grades:
    print(student)
    print(student_grades[student])
    print(" ")





travel_log = {
    "France": ["Paris", "Lillie", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
} 

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])




travel_log = {
    "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
  },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
  },
}

print(travel_log["Germany"]["cities_visited"][2])





lances = {}

print(r'''                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\ ''')

print("Bem vindo ao Leilão Secreto")
mais_compradores = True
while True:
    nome = input("Digite seu Nome: ").lower()
    valor = input("Quanto quer pagar: ")
    
    if nome in lances:
        nome =  nome +  " " + input("Já tem uma pessoa com esse nome. Coloque seu Sobrenome: ").lower()
        lances[nome] = int(valor)
    else:
        lances[nome] = int(valor)
    
    



   
    
    resposta = input("Vão ter mais compradores? [s][n] ").lower().strip()
    print("\n" * 100)
    while resposta not in ["s", "n"]:
        print("Você digitou a resposta errada")
        resposta = input("Vão ter mais compradores? [s][n] ").lower().strip()
        print("\n" * 100)
        
    if resposta == "n":
        break



lance_anterior = lances[nome]
for nome_lance in lances:
    if lances[nome_lance] > lance_anterior:
        maior_lance = lances[nome_lance]
        vencedor = nome_lance
        lance_anterior = lances[nome_lance]
    else:
        lance_anterior = lances[nome_lance]
        continue

vencedor = vencedor.title()
        
print(f"O vencedor é {vencedor} com o lance de R$ {maior_lance} ")
    
    