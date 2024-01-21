
from Winning_Clauses import *
from Straights import get_straights, ones_to_aces

# Converts symbols to numbers
def symbol_to_number(hand):
    for i, card in enumerate(hand):
        temp_list = list(card)
        if temp_list[0] == "A":
            temp_list[0] = 14
        elif temp_list[0] == "K":
            temp_list[0] = 13
        elif temp_list[0] == "Q":
            temp_list[0] = 12
        elif temp_list[0] == "J":
            temp_list[0] = 11
        else:
            temp_list[0] = int(temp_list[0])
        hand[i] = tuple(temp_list)

    return sorted(hand)

# Creates a tuple with 2 dictionaries inside, one counts the number of times a card value occurs. The other dict counts the number of times a suit occurs
def count_cards(hand):
    number_dict = {}
    suit_dict = {}
    for card in hand:
        num = card[0]
        if num in number_dict:
            number_dict[num]= number_dict[num] + 1
        else:
            number_dict[num] = 1

    for card in hand:
        suit = card[1]
        if suit in suit_dict:
            suit_dict[suit]= suit_dict[suit] + 1
        else:
            suit_dict[suit] = 1
    
    return(number_dict, suit_dict)



def calculate_hand(hand):
    hand = symbol_to_number(hand)
    card_count = count_cards(hand)
    face_values = card_count[0]
    suits = card_count[1]

    if len(face_values) >= 5:
        result = get_straights(hand)
        return result
        hand = ones_to_aces(hand)


    if get_suit(suits):
        result = get_flush(hand,suits)
    elif get_quad(face_values):
        result = four_kind(hand,face_values)
    elif get_triple(face_values) and len(face_values) <= 4:
        result = fullhouse(hand, face_values)
    elif get_triple(face_values):
        result = three_kind(hand, face_values)
    elif len(get_pairs(face_values)) > 1:
        result = two_pair(hand, face_values)
    elif len(get_pairs(face_values)) == 1:
        result = one_pair(hand, face_values)
    else:
        result = get_high_card(hand)
    return(result)


lst = [("10", "H"), ("11", "H"), ("12", "H"), ("13", "H"), ("13", "S"), ("14", "S"), ("14", "H")]
print(calculate_hand(lst))