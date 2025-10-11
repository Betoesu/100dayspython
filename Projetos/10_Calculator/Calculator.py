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


    


        