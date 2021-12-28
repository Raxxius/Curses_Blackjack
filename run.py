# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
# from art import card

def mixs(num):
    try:
        ele = int(num)
        return (1, ele, '')
    except ValueError:
        return (0, num, '')

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

def card_sum(player_cards):
    player_total = 0
    print(player_total)
    print(player_cards)
    player_cards.sort(key = mixs, reverse = True)
    print(player_cards)
    for card in player_cards:
        print(card)
        if card == "Ace":
            if player_total + 11 < 22:
                player_total += 11
                print(player_total)
            else: player_total += 1
            print(player_total)
        elif card in ["Jack", "King", "Queen"]:
            player_total += 10
            print(player_total)
        else:
            print(card)
            player_total += card
            print(player_total)
    print(f"Player total score = {player_total}")


def draw(deck):

    player_turn_end = False
    player_cards = []
    player_cards.append(deck.pop(len(deck)-1))
    card_number = len(player_cards)
    player_total = card_sum(player_cards)
    while player_turn_end is not True:
        if card_number == 5:
            player_turn_end == True
        else:
            player_card_1 = deck.pop(len(deck)-1)
            print(player_card_1)
            card_number += 1
            player_turn_end == True

player_cards = ["Queen", 3, "Ace", 7]
card_sum(player_cards)