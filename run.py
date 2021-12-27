# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

suite = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
deck_of_cards = ["hearts", "diamonds", "clubs", "spades"]

def deck():
    deck = []
    number_of_packs = 4
    for house in deck_of_cards:
        for card in suite:
            deck.append(f"{house} {card}")
    print(deck)
    print(len(deck))

deck()

