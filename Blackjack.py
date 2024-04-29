import random

card_suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
list_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = [(card, suit) for suit in card_suits for card in list_of_cards]
dealer_choices = ["hit", "stand"]
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
dealer_cards = [deck.pop(), deck.pop()]
dealer_cards_total = sum(card_value(card) for card in dealer_cards)

print("Your cards: " + str(player_cards))
print("Dealer's cards: " + str(dealer_cards)) 

print("The Dealer's total is " + str(dealer_cards_total) + ".")

while True:
    if player_cards_total < 21:
        choice = input("Your total is " + str(player_cards_total) + ". Would you like to hit or stand?: ")
        if choice == "hit":
            player_cards.append(deck.pop())
            print("You've drawn a " + str(player_cards[-1]) + ".")
            player_cards_total += card_value(player_cards[-1])
            print("Your total is now " + str(player_cards_total) + ".")
        elif choice == "stand":
            print("Your final total is " + str(player_cards_total) + ".")
            break
        else:
            print("Invalid input. Please type \"hit\" or \"stand\". ")
    elif player_cards_total > 21:
        print("You have bust! Better luck next time!")
        break
    elif player_cards_total == 21:
        print("Nice! You've hit 21! Can the dealer do the same?")
        break

while True:
    if player_cards_total > 21:
        break
    elif dealer_cards_total < player_cards_total:
        dealer_cards.append(deck.pop())
        print("The Dealer has drawn a " + str(dealer_cards[-1]) + ".")
        dealer_cards_total += card_value(dealer_cards[-1])
        print("The Dealer's total is now " + str(dealer_cards_total) + ".")
    elif 21 >= dealer_cards_total > player_cards_total:
        print("The Dealer has won this round. Better luck next time.")
        break
    elif dealer_cards_total > 21:
        print("The Dealer has bust!")
        if player_cards_total <= 21:
            print("Congratulations! You've won!")
            break
        else:
            break
    elif dealer_cards_total == player_cards_total:
        print("It's a tie. Try again?")
        break
