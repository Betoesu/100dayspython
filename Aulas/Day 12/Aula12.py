enemies = 1

def increase_enemies():
    enemies = 2 
    print(F"enemies inside function : {enemies}")
    return enemies

enemies = increase_enemies()

print(F"enemies inside function : {enemies}")

def is_prime(num):
    soma_divisiveis = 0
    for number in range (num):
        prime = num % (number + 1)
        if prime == 0:
            soma_divisiveis += 1 
    if soma_divisiveis == 2:
        return True
    else: 
        return False

numero = int(input("Numero: "))
print(is_prime(numero))
