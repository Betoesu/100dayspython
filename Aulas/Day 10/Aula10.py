
def format_name(f_name, l_name):
    """It makes every name starts with Upper Case"""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"




print(format_name(input("First name: "), input("Last name: ")))


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
               return True
            else:
                return False    
        else: 
            return True
    else:
        return False
        


print(is_leap_year(int(input("Year: "))))

len()

def solicitar_operador():
    print('''Escolha a Operação
+
-
*     
 /''')
    while True:
        simbolo = input("Escolha um símbolo: ").strip()
        if simbolo in ["+","-","*","/"]:
            return simbolo
        else:
            print("Você digitou o símbolo errado")



n1 = int(input("Digite seu primeiro número: "))
n2 = int(input("Digite seu segundo número: "))

simbolo = solicitar_operador()

if solicitar_operador() == "+":
    resultado = n1 + n2

elif simbolo == "-":
    resultado = n1 - n2

elif simbolo == "*":
    resultado = n1 * n2

elif simbolo == "/":
    resultado = n1 / n2


print(resultado)

continuar = input("Quer continuar calculando com esse resultado? ").lower()

while continuar in ["sim", "ss", "s", "yes"]:
    n1 = resultado
    n2 = int(input("Digite seu número: "))
    simbolo = solicitar_operador()


    if simbolo == "+":
        resultado = n1 + n2
    elif simbolo == "-":
        resultado = n1 - n2
    elif simbolo == "*":
        resultado = n1 * n2
    elif simbolo == "/":
        resultado = n1 / n2

    print(resultado)
    continuar = input("Quer continuar calculando com esse resultado? ").lower()

print(f"Esse é seu resultado final: {resultado}")
