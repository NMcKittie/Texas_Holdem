
from Winning_Clauses import *
from Straights import get_straight


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
def calculate_hand(hand):
    hand = symbol_to_number(hand)
    face_values = count_faces(hand)
    suits = count_suits(hand)

    if len(face_values) >= 5:
        result = get_straight(hand, face_values, suits)
        if result != None:
            return result

    if get_suit(suits):
        result = get_flush(hand, suits)
    elif get_quad(face_values):
        result = four_kind(hand, face_values)
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
    return (result)
