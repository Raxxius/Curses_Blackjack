import random
# from art import card


def mixs(num):
    # Sorts a mixed list, Int first (low to high) then Str (low to high) 
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
    # Adds the total of the cards in a hand
    # Sorts so that Aces are counted last to allow for
    # The two potential values of the Ace.
    player_total = 0
    
    player_cards.sort(key = mixs, reverse = True)
    card_values = []
    for card in player_cards:
        card_number = card.split()
        card_values.append(card_number[1])
    for card in card_values:
        if card == "Ace":
            if player_total + 11 < 22:
                player_total += 11
            else: player_total += 1
        elif card in ["Jack", "King", "Queen"]:
            player_total += 10
        else:
            player_total += int(card)
    return player_total


def draw(deck):
    # Draws a card from the deck and returns it and the new deck
    player_card = deck.pop(len(deck)-1)
    return player_card, deck

def game(deck):
    # Main game logic, draw up to 5 cards for the player,
    # Asks the player if they stick or hit
    # Player looses if they score over 21
    player_cards = []
    player_card_1, deck = draw(deck)
    player_card_2, deck = draw(deck)
    player_cards.append(player_card_1)
    player_cards.append(player_card_2)
    points = card_sum(player_cards)
    print(f"Your starting cards are {player_card_1}, and {player_card_2}")
    print(f"Your score is {points}")


deck = deck()
game(deck)