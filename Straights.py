from Winning_Clauses import get_suit, count_suits
from Create_Cards import get_heart
from Process_Win import get_straight, get_royal_flush, get_straight_flush


def get_sequence(dict):
    my_keys = list(dict.keys())
    my_seq = []
    for i, key in enumerate(my_keys):
        temp_seq = [key]
        for num in range(i+1, len(my_keys)):
            cur_key = my_keys[num]
            if cur_key == temp_seq[-1]+1:
                temp_seq = temp_seq + [cur_key]
            else:
                break

            if len(temp_seq) == 5:
                my_seq.append(temp_seq)
                break
    return my_seq


def possible_straights(hand, face_values, suits):
    sequences = get_sequence(face_values)
    flush_suit = get_suit(suits)
    possible_hands = []
    for sequence in sequences:
        possible_hand = []
        for num in sequence:
            temp_lst = []
            for card in hand:
                if int(card[0]) == num:
                    temp_lst.append(card)

            if len(temp_lst) > 1:
                temp_tuple = temp_lst[0]
                for duplicate in temp_lst:
                    if duplicate[1] == flush_suit[0]:
                        temp_tuple = duplicate
                temp_lst = [temp_tuple]
            if temp_lst:
                possible_hand.append(temp_lst[0])
        possible_hands.append(possible_hand)
    return possible_hands


def cal_royal_flush(possible_hands):

    possible_hand = possible_hands[-1]
    suit_dict = count_suits(possible_hand)
    suit = get_suit(suit_dict)
    if suit:
        if suit[0] == get_heart() and int(possible_hand[0][0]) == 10:
            return (possible_hand, get_royal_flush())
    return None


def cal_straight_flush(possible_hands):
    for possible_hand in reversed(possible_hands):
        suit_dict = count_suits(possible_hand)
        suit = get_suit(suit_dict)
        if suit:
            return (possible_hand, get_straight_flush())
    return None


def cal_straight(possible_hands):
    return (possible_hands[-1], get_straight())


def get_straight(my_hand, face_values, suits):
    possible_hands = possible_straights(my_hand, face_values, suits)
    if possible_hands:
        result = cal_royal_flush(possible_hands)
        if result == None:
            result = cal_straight_flush(possible_hands)
            if result == None:
                result = cal_straight(possible_hands)
        return result
    else:
        return None
