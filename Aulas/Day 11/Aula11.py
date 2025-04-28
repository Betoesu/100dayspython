import random


def quem_vence(dealer,player):
    if player > 21:
        return "Dealer Wins"
    
    elif player < 21 and dealer > 21:
        return "You Win"

    elif dealer > player and dealer <= 21:
        return "Dealer Wins"
    
    elif player > dealer and player <= 21:
        return "You win"

    elif player == dealer:
        return "Push"









cards = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


player_deck = []
for _ in range(2):
    index =  random.randint(0,len(cards) - 1)
    player_cards = cards.pop(index)
    player_deck.append(player_cards)

print(player_deck)

dealer_deck = []
for _ in range(2):
    index =  random.randint(0,len(cards) - 1)
    dealer_cards = cards.pop(index)
    dealer_deck.append(dealer_cards)

print(F"[{dealer_deck[0]}, ?]")

pontos_player = player_deck[0] + player_deck[1]
print(pontos_player)

pontos_dealer = dealer_deck[0] + dealer_deck[1]
print(pontos_dealer)

escolha = input("Digite 'y' para pegar outra carta, digite 'n' para parar: " )
if escolha == "n":
    print(f"Your cards: {player_deck}, score: {pontos_player}\n")
    print(f"Dealer cards: {dealer_deck}, score: {pontos_dealer}\n")
    print(quem_vence(pontos_dealer,pontos_player))






