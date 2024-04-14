import random

all_cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "Jack", "Jack", "Jack", "Jack",
             "Queen", "Queen", "Queen", "Queen", "King", "King", "King", "King", "Ace", "Ace", "Ace", "Ace"]

card1_value = str(random.choice(all_cards))
all_cards.remove(card1_value)

print(card1_value)

if card1_value in range(2, 11):
    print("Your first card is a " + str(card1_value) + ".")
elif card1_value == 11:
    print("Your first card is a Jack.")
elif card1_value == 12:
    print("Your first card is a Queen.")
elif card1_value == 13:
    print("Your first card is a King.")
elif card1_value == 14:
    print("Your first card is an Ace")




#def start_game():
#pass

#start = input("Hello and welcome to Jake's Casino! Right now, the only game you can play is Blackjack. To begin type \"Begin\": ")

#while start != "Begin":
    #start = input("Invalid input. Please type \"Begin\" to start the game: ")
#if start == "Begin":
    #start_game()

      