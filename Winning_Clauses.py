
from Straights import get_straights


def symbol_to_number(hand):

    for i, card in enumerate(hand):
        #print(type(card[0]))
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
        num = symbol_to_number(card[0])
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

#def s(hand_ordered):

lst = [("10", "C"), ("5", "H"), ("11", "C"), ("4", "H"), ("3", "H"), ("2", "S"), ("14", "H")]
lst = symbol_to_number(lst)

lst = get_straights(lst)
print(lst)
