import random
import time


def loading(reason):
    if reason == "Shuffling":
        for x in range(0, 5):
            load = reason + "." * x
            print(load, end="\r")
            time.sleep(0.8)
        print("\n")

    elif reason == "Dealing":
        for x in range(0, 3):
            load = reason + "." * x
            print(load, end="\r")
            time.sleep(0.45)
        print("\n")
    # print("\n")


def shuffle_deck(deck):
    loading("Shuffling")
    random.shuffle(deck)
    # time.sleep(3)
    return deck


def deal_cards(deck):

    hand = []
    hand = deck[:2]
    del deck[:2]
    return hand, deck


def reveal_hand(hand):
    hand_txt = ""
    for card in hand:
        hand_txt = hand_txt + str(card[0]) + card[1] + " "
    return hand_txt


def titlecard():
    print("\n\n***************************************\n")
    print("|                                     |\n")
    print("|          TEXAS HOLD 'EM!!!          |\n")
    print("|                                     |\n")
    print("***************************************\n\n")
    print("Remember - Minumum Bet Is 1G\n\n")


def show_hands(community_cards, house, player, end=False):
    loading("Dealing")
    if end:
        print("\nCommunity Cards: " + reveal_hand(community_cards) +
              "\nHouse: " + reveal_hand(house) +
              "\nPlayer: " + reveal_hand(player))

    else:
        print("\nCommunity Cards: " + reveal_hand(community_cards) +
              "\n" + "House:  \u2588  \u2588\n" +
              "Player: " + reveal_hand(player))


def winner(winner, result):
    print(result[0])
    winning_hand = result[0]
    winning_hand = reveal_hand(winning_hand)
    winning_statement_lst = result[1].split("_")
    winning_statement = ' '.join(winning_statement_lst)
    if winner == "player":
        print("You Win with a {}. Your winning hand is: {}".format(
            winning_statement, winning_hand))
    elif winner == "house":
        print("You lose. The house got a {}. Their winning hand is: {}".format(
            winning_statement, winning_hand))
    elif winner == "draw":
        print("It was a draw! You both got a {}".format(winning_statement))
