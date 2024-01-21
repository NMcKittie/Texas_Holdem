from Process_Win import get_4kind, get_3kind, get_flush_winning, get_fullhouse, get_high_winning, get_pair, get_two_pair


# returns the card faces which have had 2 occurrences
def get_pairs(dict):
    return [k for k, v in dict.items() if float(v) == 2]


# returns the card faces which have had 3 occurrences
def get_triple(dict):
    return [k for k, v in dict.items() if float(v) == 3]


# returns the card face which has had 4 occurrences
def get_quad(dict):
    return [k for k, v in dict.items() if float(v) == 4]


# returns the suit with a count of 5 or over
def get_suit(dict):
    return [k for k, v in dict.items() if float(v) >= 5]


def count_suits(hand):
    suit_dict = {}
    for card in hand:
        suit = card[1]
        if suit in suit_dict:
            suit_dict[suit] = suit_dict[suit] + 1
        else:
            suit_dict[suit] = 1
    return suit_dict


def count_faces(hand):
    number_dict = {}
    for card in hand:
        num = card[0]
        if num in number_dict:
            number_dict[num] = number_dict[num] + 1
        else:
            number_dict[num] = 1
    return number_dict


def find_pair(hand, num):
    pair = []
    for i, card in enumerate(hand):
        if card[0] == num:
            pair = [hand.pop(i), hand.pop(i)]
            break
    return pair


def find_triple(hand, num):
    triple = []
    for i, card in enumerate(hand):
        if card[0] == num:
            triple = [hand.pop(i), hand.pop(i), hand.pop(i)]
            break
    return triple


def get_flush(hand, dict):
    suit = get_suit(dict)[0]
    flush = []
    for card in reversed(hand):
        if suit in card:
            flush.append(card)
        if len(flush) == 5:
            return (sorted(flush), get_flush_winning())
    return None


def four_kind(hand, dict):
    num = get_quad(dict)
    four_of_a_kind = [(num, "H"), (num, "S"), (num, "D"), (num, "C"), hand[-1]]
    return (four_of_a_kind, get_4kind())


def three_kind(hand, dict):
    num = max(get_triple(dict))
    three_of_a_kind = find_triple(hand, num) + [hand[-2], hand[-1]]
    return (three_of_a_kind, get_3kind())


def one_pair(hand, dict):
    num = max(get_pairs(dict))
    pair = find_pair(hand, num) + [hand[-3], hand[-2], hand[-1]]
    return (pair, get_pair())


def two_pair(hand, dict):
    pairs = get_pairs(dict)
    first_pair = pairs.pop(pairs.index(max(pairs)))
    second_pair = pairs.pop(pairs.index(max(pairs)))
    pairs = find_pair(hand, first_pair) + \
        find_pair(hand, second_pair) + [hand[-1]]
    return (pairs, get_two_pair())


def fullhouse(hand, dict):
    pair = max(get_pairs(dict))
    triple = max(get_triple(dict))
    fullhouse = find_triple(hand, triple) + find_pair(hand, pair)
    return (fullhouse, get_fullhouse())


def get_high_card(hand):
    high_cards = []
    for card in reversed(hand):
        high_cards.append(card)
        if len(high_cards) == 5:
            break
    return (high_cards, get_high_winning())
