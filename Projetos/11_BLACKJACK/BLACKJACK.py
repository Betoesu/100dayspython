import random
def take_card(deck,cards):
    index =  random.randint(0,len(cards) - 1)
    card = cards.pop(index)
    deck.append(card)
    return card

def who_wins(player,dealer):
    if player > 21:
        return "Dealer Wins"
    
    elif (player <= 21) and (dealer > 21):
        return '''Dealer Bust
You Win'''

    elif (dealer > player) and (dealer <= 21):
        return "Dealer Wins"
    
    elif (player > dealer) and (player <= 21):
        return "You win"

    elif player == dealer:
        return "Push"

def show_decks(reveal_dealer=False):
    print(f"{player_deck} Your Cards")
    if reveal_dealer:
        print(f"{dealer_deck} Dealer Cards")
    else:
        print(f"[{dealer_deck[0]}, ?] Dealer Cards")

def wrong_type(escolha):
    while escolha not in ["y", "n"]:
        print("Você digitou o comando errado. Tente novamente")
        escolha = input("Type 'y' to get another card, type 'n' to pass: " ).lower()
    return escolha

def As(deck):
    while sum(deck) > 21 and 11 in deck:
        deck[deck.index(11)] = 1

cards = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


player_deck = []
for _ in range(2):
    index =  random.randint(0,len(cards) - 1)
    player_card = cards.pop(index)
    player_deck.append(player_card)

if player_deck[0] == 11:
    print(f"[A, {player_deck[1]}]")
elif player_deck[1] == 11:
    print(f"[{player_deck[0]}, A]")
else:
    print(f"{player_deck} Your Cards")


dealer_deck = []
for _ in range(2):
    index =  random.randint(0,len(cards) - 1)
    dealer_card = cards.pop(index)
    dealer_deck.append(dealer_card)

if dealer_deck[0] == 11:
    print(f"[A, ?]")
else:
    print(F"[{dealer_deck[0]}, ?] Dealer Cards")



pontos_player = player_deck[0] + player_deck[1]
As(player_deck)
pontos_player = player_deck[0] + player_deck[1]



pontos_dealer = dealer_deck[0] + dealer_deck[1]
As(dealer_deck)
pontos_dealer = dealer_deck[0] + dealer_deck[1]


if pontos_player == 21:
    input(" ")
    print("BLACKJACK!!!")
    show_decks(reveal_dealer=True)
    print(" ")
    print(who_wins(pontos_player,pontos_dealer))  
    exit()      


escolha = input("Digite 'y' para pegar outra carta, digite 'n' para parar: " ).lower()
escolha = wrong_type(escolha)
print(" ")

if escolha == "n":
    show_decks(reveal_dealer=True)
    print(" ")
    
    while pontos_dealer < pontos_player:
        new_card = take_card(dealer_deck,cards)
        pontos_dealer += new_card
        As(dealer_deck)
        pontos_dealer = sum(dealer_deck)

        print("O Dealer compra outra carta\n")
        show_decks(reveal_dealer=True)
        print(" ")
    print(who_wins(pontos_player,pontos_dealer))
    

elif escolha == "y":
    new_card = take_card(player_deck, cards)
    pontos_player += new_card
    As(player_deck)
    pontos_player = sum(player_deck)


    while pontos_player < 21:
        show_decks()
        escolha = input("Digite 'y' para pegar outra carta, digite 'n' para parar: " ).lower()
        escolha = wrong_type(escolha)
        print(" ")

        if escolha == "n":
            show_decks(reveal_dealer=True)
            print(" ")
    
            while pontos_dealer < pontos_player:
                new_card = take_card(dealer_deck,cards)
                pontos_dealer += new_card
                As(dealer_deck)
                pontos_dealer = sum(dealer_deck)

                print("Dealer get another card\n")
                show_decks(reveal_dealer=True)
                print(" ")
            print(who_wins(pontos_player,pontos_dealer))
            break
            
            
        elif escolha == "y":
            new_card = take_card(player_deck, cards)
            pontos_player += new_card
            As(player_deck)
            pontos_player = sum(player_deck)

    if pontos_player > 21:
        show_decks(reveal_dealer=True)
        print("You Bust")
        print(who_wins(pontos_player,pontos_dealer))

