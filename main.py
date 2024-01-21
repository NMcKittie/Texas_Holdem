
from Display import *
from Process_Hand import calculate_hand
from Create_Cards import create_deck
from Process_Win import calculate_win


def bet_or_fold():
    user_input = input("Bet or Fold? ")
    if user_input.lower() == "bet":
        money = int(input("How much are you betting? "))
        if money < 1:
            money = 1
    else:
        money = 0
    return money


def game_run(deck):
    while True:
        house_deck = []
        player_deck = []
        community_cards = []

        shuffled_deck = shuffle_deck(deck)

        house_deck, shuffled_deck = deal_cards(shuffled_deck)
        player_deck, shuffled_deck = deal_cards(shuffled_deck)

        show_hands(community_cards, house_deck, player_deck)

        print(bet_or_fold())

        community_cards = shuffled_deck[:3]
        del shuffled_deck[:3]

        show_hands(community_cards, house_deck, player_deck)

        print(bet_or_fold())

        community_cards = community_cards + shuffled_deck[:1]
        del shuffled_deck[:1]
        show_hands(community_cards, house_deck, player_deck)

        print(bet_or_fold())

        community_cards = community_cards + shuffled_deck[:1]
        del shuffled_deck[:1]

        show_hands(community_cards, house_deck, player_deck)

        print(bet_or_fold())

        house_result = calculate_hand(community_cards + house_deck)
        player_result = calculate_hand(community_cards + player_deck)

        show_hands(community_cards, house_deck, player_deck, end=True)
        calculate_win(player_result, house_result)
        break


def main():

    deck = create_deck()
    Bank = 100

    titlecard()

    while True:
        game_run(deck)
        user_input = input("Want to play again? (yes/no) ")
        if user_input.lower() == "no":
            break


if __name__ == "__main__":
    main()
