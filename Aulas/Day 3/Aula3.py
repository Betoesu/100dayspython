print("Welcome to rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? "))
    if age <= 12:
        bill = 5
        print(" Child tickets are $5")
    elif age > 12 and age <= 18:
        bill = 7
        print(" Youth tickets are $7")   
    else:
        bill = 12
        print("Adult tickets are $12")
        
    wants_photo = input("Do you want to have to have a photo take? Type y for Yes and n for No. ")
    if wants_photo == "y": 
        #Add $3 to their bill
        bill += 3
        
    print(f"Your final bill is {bill}")   
else:
    print("Sorry you have to grow taller before you can ride")
    


 
print("Welcome to the Odd or Even!!!")
number = int(input("Type a number: "))

if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")
    
    
print("Welcome to the Freedy Fazbear Pizzaria")
bill = 0
size = input("Which size of pizza do you want? Small, Medium or Large (S, M or L): ")
if size == "S":
    bill += 15
    pepperoni = input("Do you want pepperoni in your pizza? Y or N: ") 
    if pepperoni == "Y" or "y":
        bill += 2 
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == "Y":
            bill += 1   
elif size == "M":
    bill += 20
    pepperoni = input("Do you want pepperoni in your pizza? Y or N: ") 
    if pepperoni == "Y" or "y":
        bill += 3
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == "Y":
            bill += 1     
elif size == "L":
    bill += 25
    pepperoni = input("Do you want pepperoni in your pizza? Y or N: ") 
    if pepperoni == "Y" or "y":
        bill += 3
        extra_cheese = input("Do you want extra cheese? Y or N: ")
        if extra_cheese == "Y":
            bill += 1   
else:
    print("You typed the wrongs inputs")    
print(f"Your final bill is {bill}")

print(''' .:'                           `:.
     ::'                                   `::
     :: :.                               .: ::
    `:. `:.             .             .:'  .:'
     `::. `::           !           ::' .::'
       `::.`::.    .' ! `.    .::'.::'
         `:.  `::::'':!:``::::'   ::'
         :'*:::.  .:' ! `:.  .:::*`:
        :: HHH::.   ` ! '   .::HHH ::
       ::: `H TH::.  `!'  .::HT H' :::
       ::..  `THHH:`:   :':HHHT'  ..::
       `::      `T: `. .' :T'      ::'
         `:. .   :         :   . .:'
           `::'               `::'
             :'  .`.  .  .'.  `:
             :' ::.       .:: `:
             :' `:::     :::' `:
              `.  ``     ''  .'
               :`...........':
               ` :`.     .': '
                `:  `"""'  :''')
print("Bem Vindo ao Castelo de Raya")
print('''Você se encontra aqui pois um dos cavalos dos espiões do seu reino voltou sozinho com uma carta que dizia. [O solo me traz medo] [Quanto mais alto o sonho, maior a queda. Se não sabe dançar não vá dançar] [Quanto mais alimentado maior é]
        Ninguem entendia pois as frases estavam escritas aleátoriamente pela folha e não faziam nenhum sentido aparente, mas você sabia que iria precisar delas para sua aventura''')
print("Sua missão como Arqueiro é espionar e trazer informações sobre as intenções de Raya e seus servos")
print("Você está a uma boa distância do Castelo aparentemente abandonado")
escolha1 = input('''O que deseja fazer? Digite 1, 2 ou 3
    1) Chegar mais perto e tentar furtivamente ir pela porta da frente
    2) Rodear o Castelo para tentar achar outra entrada
    3) Escalar uma árvore alta para entrar pela janela mais próxima 
    
    ''')
if escolha1 == "1":
    print("Você avança e não percebe a presença de ninguém. Ao abrir a porta da frente sente a presença de duas figuras atras de você, antes mesmo de poder virar. VOCÊ MORRE")
    input("Pressione Enter para sair...")
elif escolha1 == "2":
    print('''Você consegue rodear o castelo furtivamente, quando você olha para a parte de trás do castelo percebe que ele parece um pouco maior e mais amedontrador. E então começa a olhar em volta e percebe que já está em outro lugar, devido a sua 
experiência como arqueiro, percebe que havia um feitiço em volta desse castelo, e agora aquela frase estranha 'O solo me traz medo' faz todo sentido. Você passará o resto da sua vida numa realidade paralela perdido. VOCE MORREU''')
    input("Pressione Enter para sair...")
elif escolha1 == "3":
    print("Devido a sua habilidade como arqueiro você sobe na árvore com extrema facilidade e furtividade e consegue efetivamente entrar no castelo")
    print("Você está adiante de uma grande porta semi-aberta e uma escada, na parte de baixo há o hall de entrada onde parecia ocorrer muitos bailes e a parte de cima a escada é tão grande que não se ve o fim, mas se ve quartos e mais quartos")
    escolha2 = input('''O que deseja fazer? Digite 1,2 ou 3
                     1) Subir a Escada
                     2) Abrir a porta
                     3) Descer a Escada
                     
                     ''')
    if escolha2 == "1":
        print('''       Você começa a subir a aparente interminável escada sem ir para os quartos, pois havia iluminação neles, então decide continuar subindo quando se depara. RAYA. O dragão estranhamente consciente só com sua presença te paraliza e antes
mesmo de pensar que ' Quanto mais alto o sonho maior a queda' tinha um motivo, você já está morto. VOCÊ MORREU ''')
        input("Pressione Enter para sair...")
    elif escolha2 == "3":
        print("Você desce para o Hall, e começar a tocar uma música, uma sinfonia bonita, mas naquele ambiente escuro e abandonado, era aterrorizante. Até que começa a ver no fundo da escuridão silhuetas, não são 10, nem 20, são tantas que nem consegue contar. E quanto mais a música toca mais eles se aproximam, cercando você. VOCÊ MORREU")
        input("Pressione Enter para sair...")
    elif escolha2 == "2":
        print('''Você abre a porta lentamente, quando percebe um Kalkara [Têm a aparência semelhante a um urso gigante, mas com traços e hábitos de um macaco, sua agilidade, apesar do seu tamanho, é gigantesca. Um predador nato com uma pele escamosa,
negra e impenetrável], você começa a sentir frio de tanto medo, e seu coração dispara rapidamente, você como arqueiro sabe muito bem o quão letais são essas criaturas, mas lembra de seu treinamento, e PRECISA agir. Ao rapidamente 
voltar a racionalidade você rapidamente observa a sala, ela é iluminada por tochas há uma janela aonde você pode fugir devido a grande árvore lá fora, e o mais importante o Kalkara está a frente de uma mesa onde está o pergaminho de
 comunicação das guerrilhas de RAYA. Esse pergaminho levaria seu povo a vencer essa terrível guerra''')
        
        escolha3 = input(''' O que deseja fazer? Digite 1,2 ou 3. Lembre sua vida e vitória do seu reino dependem disso
                        1) Pegar óleo da sua bolsa e incendear sua flecha e disparar contra o Kalkara
                        2) Pegar sua adaga extremamente resistente e afiada e tentar um ponto vital já que ele se encontra de costas, e ainda não percebeu sua presença
                        3) Chamar a atenção do Kalkara atirando-o uma flecha, e tentar prever seu ataque, esquivar e pergar o pergaminho e fugir
                        
                        ''')
        if escolha3 == "3":
            print('''Você atira no Kalkara e ele sente o impacto, mas nem sequer demonstra dor, ele se vira para você e você percebe seus olhos vermelhos, são bem mais macabros do que nos livros. Você percebe ele vindo para te atacar, você desvia e 
                  corre para pegar o pergaminho, quando é paralizado, e ao olhar para seu peito ve 5 garras, e percebe o como realmente apesar do seu tamanho ser maior que de um urso, sua agilidade é como a de um macaco. VOCÊ MORREU''')
            input("Pressione Enter para sair...") 
        elif escolha3 == "2":
            print('''Você vai lentamente, tentando não ser percebido pela grande figura. Avança rapidamente e finca sua adaga no pescoço do Kalkara, e consegue ouvir seu grito de dor, e é aterrorizante, é diferente de tudo o que ja ouviu. O Kalkara 
sentindo dor, se vira para você, e é notório o ódio esboçado em um complexo olhar e uma respiração pesada, você se questiona como essa terrível criatura está viva, mas passa pela sua cabeça a ideia de que a pele quase impenetrável
do Kalkara foi penetrada, mas talvez não o suficiente para chegar em um ponto vital. Em questão de um piscar de olhos você o vê com sua pata vindo lentamente em direção ao seu rosto, então você se enxerga no chão e vê seu próprio 
corpo decapitado nesse curto período de tempo. VOCÊ MORREU''')
            input("Pressione Enter para sair...")
        elif escolha3 == "1":
            print('''Você rapidamente pega um pote de óleo e derrama sobre sua melhor flecha, esta indo em direção à tocha, quando escuta fungadas pesadas, é o Kalkara, como um grande predador, tem um ótimo faro. Você percebendo que ele em questão 
de segundos  vai notar sua presença corre, incendeia sua flecha e se vira, a sua visão é um grande arco, uma flecha flamejante, e apesar de em plano de fundo, é o que mais chama atencão, o olhar frio, amedontrador e estranhamente 
vermelho do Kalkara.  Mas tem uma coisa errada, ele não veio pra cima, é como ver um predador evitando a presa, mas por que? POR QUE? Ele tem um plano? Ele está se preparando? Que me dar medo? Medo? É ai quando tudo faz sentido na
sua cabeça, [Quanto mais se  alimenta, maior é]. É FOGO. Logo eu acertei realmente é medo, mas não meu, você tem medo Kalkara. Mas apesar desse rápido pensamento ter ocorrido num longo um segundo, o Kalkara avança mesmo com medo, 
pois é um predador nato, sabendo que precisa agir mesmo em   medo. Mas para você os movimentos dele se tornaram lento, você vê essa cena lentamente como se fosse morrer, mas não é você que vai. Você dispara a flecha e percebe 
rapidamente o fogo se espalhando diante a figura enorme, e seus gritos    aterrorizantes de dor. O Kalkara ainda vem em sua direção mas você rapidamente desvia e corre para o pergaminho, assim que olha para trás vé o Kalkara em 
chamas no chão e aquele quarto que antes era explêndido, agora está consumido pelo fogo.''')
            escolha4 = input('''Você está em frente a janela e existe uma grande árvore lá fora, o fogo se espalha rapidamente o que fazer?
                             1) Quebrar a janela com seu arco com cuidado e depois pular
                             2) Pular quebrando a janela com seu salto
                             3) Tentar conter o fogo para sair pela porta que entrou
                             
                             ''')
            if escolha4 ==  "1":
                print('''Você corre pela janela, quebra ela com seu arco para não se ferir com os estilhaços e sente o fogo mem seu pé, mas pula rapidamente e desce a grande árvore numa facilidade, chama o seu fiel cavalo e corre em direcão ao seu
 reino, atrás de você aquele antes castelo frio e escuro agora quente e iluminado por chamas, e na sua mão um simples papel que vai levar o seu povo a vitória sobre a grande maldade de Raya. Ou será que a vitória somente de um 
das muitas guerras? Isso não importa agora, importa que por sua causa seu povo não perecerá tão cedo. VITÓRIA''')
                input("Pressione Enter para sair...")
            elif escolha4 == "2":
                print(''''Você corre pela janela, pula sem pensar duas vezes, desce a grande árvore numa facilidade, chama o seu fiel cavalo e corre em direcão ao seu reino, atrás de você aquele antes castelo frio e escuro agora quente e iluminado 
por chamas, e na sua mão um simples papel que vai levar o seu povo a vitória sobre a grande maldade de Raya. Ou será que a vitória somente de um das muitas guerras?
     Isso não importa agora, importa que por sua causa seu povo não perecerá tão cedo. VITÓRIA''')
                input("Pressione Enter para sair...")
            elif escolha4 == "3":
                print('''O fogo está descontrolado, mas mesmo assim você desobedece todo seu treinamento e sabedoria de saber lidar em situações como essa e tenta sair pela porta que entrou, o percebe que já tem muito fogo e precisa voltar,
quando olha para trás o caminho que veio já foi tomado por fogo, então você observa lentamente sua morte e seu povo perecer devido a sua inprudência. VOCÊ MORREU''')
                input("Pressione Enter para sair...")
            else: print("Digite o número certo")
        else: print("Digite o número certo")
    else:
         print("Digite o número certo")       
else:
    print("Digite o número certo")
