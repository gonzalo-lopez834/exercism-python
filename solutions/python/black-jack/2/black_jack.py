def value_of_card(card):
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 1
    return int(card)

def higher_card(card_one, card_two):
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)
    if v1 > v2:
        return card_one
    if v2 > v1:
        return card_two
    return card_one, card_two

def value_of_ace(card_one, card_two):
    # En esta función, el As en mano cuenta como 11
    v1 = 11 if card_one == 'A' else value_of_card(card_one)
    v2 = 11 if card_two == 'A' else value_of_card(card_two)
    
    # Si sumamos 11 y no nos pasamos de 21, el nuevo As vale 11
    if v1 + v2 + 11 <= 21:
        return 11
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