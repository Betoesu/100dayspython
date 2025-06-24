from data_high_lower import data
import random
import wrong_type



print(''' 
  _    _ _____ _____ _    _              
 | |  | |_   _/ ____| |  | |             
 | |__| | | || |  __| |__| |             
 |  __  | | || | |_ |  __  |             
 | |  | |_| || |__| | |  | |             
 |_|  |_|_____\_____|_|  |_|_____ _____  
 | |    / __ \ \        / /  ____|  __ \ 
 | |   | |  | \ \  /\  / /| |__  | |__) |
 | |   | |  | |\ \/  \/ / |  __| |  _  / 
 | |___| |__| | \  /\  /  | |____| | \ \ 
 |______\____/   \/  \/   |______|_|  \_\
                                         
                                        
''')


answer = ""
right_answer = ""
score = 0
# O candidato vencedor vira o candidato A na proxima
a = data[random.randint(0,len(data) - 1)]
while answer == right_answer:
  b = data[random.randint(0,len(data) - 1)]

  #Maneira de evitar que sejam a mesma pessoa
  while a == b:
      b = data[random.randint(0,len(data) - 1)]
  print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")

  print(''' 
  __      _______ 
  \ \    / / ____|
    \ \  / / (___  
    \ \/ / \___ \ 
      \  /  ____) |
      \/  |_____/ 
                  
                  
  ''')

  print(f"Compare B: {b["name"]}, a {b["description"]}, from {b["country"]}")
  question = "Who has more follower? Type 'A' or 'B': "
  answer = input(question).lower()

  #Únicas respostas possíveis
  right_type = ["a", "b"]

  #Função para evitar que o usuário digite o comando errado
  answer = wrong_type.wrong_type(answer,right_type,question,"english")

  if a["follower_count"] > b["follower_count"]:
      right_answer = "a"
      winner = a
      #deleta o candidato B da lista
      del data[data.index(b)]


  else:
      right_answer = "b"
      winner = b 
      # deleta o candidato A da lista
      del data[data.index(a)]
      

  if answer == right_answer:
      score += 1
      print(f"You are right! Current Score: {score}")
      print("\n" * 20)
      a = winner 

  else:
      print(f"Sorry, That's wrong. Final Score: {score}")
