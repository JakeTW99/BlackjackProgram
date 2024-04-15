import random

all_cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "Jack", "Jack", "Jack", "Jack",
             "Queen", "Queen", "Queen", "Queen", "King", "King", "King", "King", "Ace", "Ace", "Ace", "Ace"]

player_card1 = random.choice(all_cards)
all_cards.remove(player_card1)
player_card2 = random.choice(all_cards)
all_cards.remove(player_card2)

if player_card1 == "Ace":
    print("Your first card is an " + str(player_card1) + ".")
else:
    print("Your first card is a " + str(player_card1) + ".")
if player_card2 == "Ace":
    print("Your second card is an " + str(player_card2) + ".")
else:
    print("Your second card is a " + str(player_card2) + ".")

#def start_game():
#pass

#start = input("Hello and welcome to Jake's Casino! Right now, the only game you can play is Blackjack. To begin type \"Begin\": ")

#while start != "Begin":
    #start = input("Invalid input. Please type \"Begin\" to start the game: ")
#if start == "Begin":
    #start_game()

      