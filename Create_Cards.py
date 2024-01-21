

def get_club():
    return "\u2663"


def get_heart():
    return "\u2661"


def get_diamond():
    return "\u2662"


def get_spade():
    return "\u2660"


def create_deck():
    suits = [get_heart(), get_diamond(), get_spade(), get_club()]
    numbers = ["2", "3", "4", "5", "6", "7",
               "8", "9", "10", "J", "Q", "K", "A"]
    deck = []
    for number in numbers:
        for suit in suits:
            deck.append((number, suit))
    return deck
