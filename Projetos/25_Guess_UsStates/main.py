import  pandas
from turtle import Turtle, Screen

#Aqui eu começo inicializando uma tela da biblioteca turtle
screen = Screen()
screen.title("U.S States Game")

#Salvo a imagem que esta neste path abaixo
image = "./Projetos/25_Guess_UsStates/blank_states_img.gif"
screen.addshape(image)
imageTurtle = Turtle()
imageTurtle.shape(image)

#Leio o arquivo dos estados do USA e transformo em lista
data = pandas.read_csv("./Projetos/25_Guess_UsStates/50_states.csv")
stateName = data.state
stateName = stateName.to_list()



#Crio um input pra aparecer na screen e começo um contador de estados corretos
answerState = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
correctState = 0

#Começo um loop que a única condição para parar é digitar exit ou acertar os 50 estadis
while True:
    if answerState == "Exit":
        #Aqui quando o usuário decidir parar ou acertar todos, é criado um arquivo dos estados que ele não escreveu
        statesToLearn = pandas.DataFrame(stateName)
        statesToLearn.to_csv("./Projetos/25_Guess_UsStates/States_to_Learn.csv")
        break
        
    #Aqui confiro se a resposta do usuario esta na lista dos estados.
    if answerState in stateName:
        #Procuro saber onde na lista esta o estado que o usuário acertou
        stateIndex = stateName.index(answerState)
        #E depois o retiro da lista e somo um ponto no correctState
        stateName.pop(stateIndex)
        correctState += 1       

        #Procuro o x e y do estado no arquivo dos estados para levar o nome do estado correto ate o lugar onde ele fica na imagem. Obs: Transformo em lista para que na hora de usar o .goto ele sair como inteiro
        xState = data.x[data.state == answerState].tolist()
        yState = data.y[data.state == answerState].tolist()

        
        
        stateTurtle = Turtle()
        stateTurtle.hideturtle()
        stateTurtle.penup()
        #Aqui puxo de dentro da lista que criei do x e y
        stateTurtle.goto(xState[0],yState[0])
        stateTurtle.write(answerState)
    answerState = screen.textinput(title=f"{correctState}/50", prompt="What's another state's name?").title()

    if correctState == 50:
        break

#Aqui quando o usuário decidir parar ou acertar todos, é criado um arquivo dos estados que ele não escreveu
statesToLearn = pandas.DataFrame(stateName)
statesToLearn.to_csv("./Projetos/25_Guess_UsStates/States_to_Learn.csv")

screen.bye()
