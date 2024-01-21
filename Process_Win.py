from Display import winner


def get_royal_flush():
    return "Royal_Flush"


def get_straight_flush():
    return "Straight_Flush"


def get_4kind():
    return "Four_of_a_Kind"


def get_fullhouse():
    return "Full_House"


def get_flush_winning():
    return "Flush"


def get_straight():
    return "Straight"


def get_3kind():
    return "Three_of_a_Kind"


def get_two_pair():
    return "Two_Pairs"


def get_pair():
    return "Pair"


def get_high_winning():
    return "High_Card"


def combo_value(combo):
    value = 0
    if combo == get_royal_flush():
        value = 10
    elif combo == get_straight_flush():
        value = 9
    elif combo == get_4kind():
        value = 8
    elif combo == get_fullhouse():
        value = 7
    elif combo == get_flush_winning():
        value = 6
    elif combo == get_straight():
        value = 5
    elif combo == get_3kind():
        value = 4
    elif combo == get_two_pair():
        value = 3
    elif combo == get_pair():
        value = 2
    else:
        value = 1
    return value


def calculate_win(player_result, house_result):
    player_score = combo_value(player_result[1])
    house_score = combo_value(house_result[1])

    if player_score > house_score:
        winner("player", player_result)
    elif house_score > player_score:
        winner("house", house_result)
    elif house_score == player_score:
        if player_score > 1:
            if int(player_result[0][0][0]) > int(house_result[0][0][0]):
                winner("player", player_result)
            elif int(player_result[0][0][0]) < int(house_result[0][0][0]):
                winner("house", house_result)
            else:
                winner("draw", player_result)
        else:
            if int(player_result[0][0][-1]) > int(house_result[0][0][-1]):
                winner("player", player_result)
            elif int(player_result[0][0][-1]) < int(house_result[0][0][-1]):
                winner("house", house_result)
            else:
                winner("draw", player_result)


player_result = ([('5', '\u2661'), ('6', '\u2661'),
                 ('7', '\u2661'), ('8', '\u2661'), ('9', '\u2661')], "Straight_Flush")

house_result = ([('9', '\u2661'), ('9', '\u2660'),
                 ('7', '\u2661'), ('8', '\u2662'), ('11', '\u2661')], "Pair")

calculate_win(player_result, house_result)
