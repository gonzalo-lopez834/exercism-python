"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):

    if card in ['J', 'Q', 'K']:
        return 10
    elif card in ['A']:
        return 1
    else: 
        return int(card)


def higher_card(card_one, card_two):

    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if v1 > v2:
        return card_one
    elif v1 < v2:
        return card_two
    else: 
        return card_one, card_two 


def value_of_ace(card_one, card_two):

    if card_one == 'A':
        v1 = 11
    elif card_one in ['J', 'Q', 'K']:
        v1 = 10
    else:
        v1 = int(card_one)

    if card_two == 'A':
        v2 = 11
    elif card_two in ['J', 'Q', 'K']:
        v2 = 10
    else:
        v2 = int(card_two)

    total = v1 + v2 

    if (total + 11) <= 21:
        return 11
    else: 
        return 1 
 


def is_blackjack(card_one, card_two):
    tens = ['10', 'J', 'Q', 'K']
    return (card_one == 'A' and card_two in tens) or \
           (card_two == 'A' and card_one in tens)

def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in [9, 10, 11]
