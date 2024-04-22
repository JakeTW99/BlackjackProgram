import random

card_suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
list_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = [(card, suit) for suit in card_suits for card in list_of_cards]

def card_value(card):
    if card[0] in ["Jack", "Queen", "King"]:
        return 10
    elif card[0] == "Ace":
        return 11
    else:
        return int(card[0])

random.shuffle(deck)

player_cards = [deck.pop(), deck.pop()]
player_cards_total = sum(card_value(card) for card in player_cards)

print(player_cards)

while True:
    if player_cards_total < 21:
        choice = input("Your total is " + str(player_cards_total) + ". Would you like to hit or stand?: ")
        if choice == "hit":
            player_cards.append(deck.pop())
            print(player_cards[-1])
            player_cards_total += card_value(player_cards[-1])
            print("Your total is now " + str(player_cards_total) + ".")
        elif choice == "stand":
            print("Your final total is " + str(player_cards_total) + ".")
            break
        else:
            print("Invalid input. Please type \"hit\" or \"stand\". ")
    elif player_cards_total == 21:
        print("Congratulations! You've won!")
        break
    elif player_cards_total > 21:
        if ("Ace", 11) in player_cards:
            player_cards_total -= 10
            continue
        else:
            print("You have bust! Better luck next time!")
            break