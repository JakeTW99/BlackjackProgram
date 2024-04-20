import random

card_suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
list_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = [(card, suit) for suit in card_suits for card in list_of_cards]

#print(deck)

def card_value(card):
    if card == "Jack":
        return 10
    elif card == "Queen":
        return 10
    elif card == "King":
        return 10
    elif card == "Ace":
        return 11
    else:
        return int((card))

#print (card_value("Jack"))

random.shuffle(deck)

player_cards = [deck.pop(), deck.pop()]

#print("You have a " + player_cards[0] + ".")
#print("You have a " + player_cards[1] + ".")

print("Your first card is: (player_cards[0])")

