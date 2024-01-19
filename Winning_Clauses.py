
def symbol_to_number(symbol):
    if symbol == "A":
        return 14
    elif symbol == "K":
        return 13
    elif symbol == "Q":
        return 12
    elif symbol == "J":
        return 11
    else:
        return int(symbol)


def check_sequence(a_dict):
    print(a_dict)
    mykeys = list(a_dict.keys())

    mykeys.sort()

    count = 0
    first_val = mykeys[0]
    for a in mykeys:
        if first_val + count == a:
            count += 1
        else:
            return False
    return True


def count_cards(hand):
    number_dict = {}
    suit_dict = {}
    for card in hand:
        num = symbol_to_number(card[:-1])
        if num in number_dict:
            number_dict[num]= number_dict[num] + 1
        else:
            number_dict[num] = 1

    for card in hand:
        suit = card[-1]
        if suit in suit_dict:
            suit_dict[suit]= suit_dict[suit] + 1
        else:
            suit_dict[suit] = 1
    
    return(number_dict, suit_dict)

#def s(hand_ordered):


tup = count_cards(["KD", "QL", "AL", "10J"])
print(tup)
print(check_sequence(tup[0]))