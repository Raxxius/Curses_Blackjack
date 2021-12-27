# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
# from art import card


def deck():
    # Creates the deck of cards based on 4 packs of cards 
    suite = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    deck_of_cards = ["Hearts", "Diamonds", "Clubs", "Spades"]
    deck = []
    number_of_packs = 4
    for i in range(number_of_packs):
        for house in deck_of_cards:
            for card in suite:
                deck.append(f"{house} {card}")
    random.shuffle(deck)
    return deck

def draw(deck):
    card_number = 0
    player_turn_end = False
    while player_turn_end != True:
        if card_number == 5:
            player_turn_end == True
        else:
            player_card_1 = deck.pop(len(deck)-1)
            print(player_card_1)
            card_number += 1
            player_turn_end == True

deck = deck()
print("Deck is shuffled")
draw(deck)