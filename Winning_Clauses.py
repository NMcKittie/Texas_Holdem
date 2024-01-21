
def get_pairs(dict):
    return [k for k,v in dict.items() if float(v) == 2]

def get_triple(dict):
    return [k for k,v in dict.items() if float(v) == 3]

def get_quad(dict):
    return [k for k,v in dict.items() if float(v) == 4]

def get_suit(dict):
    return [k for k,v in dict.items() if float(v) >= 5]


def find_pair(hand, num):
    pair = []
    for i, card in enumerate(hand):
        if card[0] == num:
            pair = [hand.pop(i),hand.pop(i)]
            break
    return pair

def find_triple(hand, num):
    triple = []
    for i, card in enumerate(hand):
        if card[0] == num:
            triple = [hand.pop(i),hand.pop(i),hand.pop(i)]
            break
    return triple

def get_flush(hand, dict):
    suit = get_suit(dict)[0]
    flush = []
    for card in reversed(hand):
        if suit in card:
           flush.append(card) 
        if len(flush) == 5:
            return (sorted(flush), "Flush")
    return None

def four_kind(hand, dict):
    num = get_quad(dict)
    four_of_a_kind = [(num, "H"), (num, "S"), (num, "D"), (num, "C"), hand[-1]]
    return (four_of_a_kind, "Four_of_a_Kind")

def three_kind(hand, dict):
    num = max(get_triple(dict))
    three_of_a_kind = find_triple(hand,num) + [hand[-2], hand[-1]]
    return (three_of_a_kind, "Three_of_a_Kind")


def one_pair(hand, dict):
    num = max(get_pairs(dict))
    pair = find_pair(hand,num) + [hand[-3], hand[-2], hand[-1]]
    return (pair, "Pair")

def two_pair(hand, dict):
    pairs = get_pairs(dict)
    first_pair = pairs.pop(pairs.index(max(pairs)))
    second_pair = pairs.pop(pairs.index(max(pairs)))
    pairs = find_pair(hand,first_pair) + find_pair(hand,second_pair) +  [hand[-1]]
    return(pairs, "Two_Pairs")


def fullhouse(hand, dict):
    pair = max(get_pairs(dict))
    triple = max(get_triple(dict))
    fullhouse = find_triple(hand,triple) + find_pair(hand,pair)
    return (fullhouse, "Full_House")


def get_high_card(hand):
    high_cards = []
    for card in reversed(hand):
        high_cards.append(card)
        if len(high_cards) == 5:
            break
    return (high_cards, "High_Card")


