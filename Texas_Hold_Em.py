import random
import time






def loading(reason):
    if reason == "Shuffling":
        for x in range(0,5):  
            load = reason + "." * x
            print (load, end="\r")
            time.sleep(0.8)  
        print("\n")
    
    elif reason == "Dealing":
        for x in range(0,3):  
            load = reason + "." * x
            print (load, end="\r")
            time.sleep(0.45)  
        print("\n")
    #print("\n")

def shuffle_deck(deck):
    loading("Shuffling")
    random.shuffle(deck)
    #time.sleep(3)
    return deck

def deal_cards(deck):
    
    hand = []
    hand = deck[:2]
    del deck[:2]
    return hand, deck

def reveal_hand(hand):
    hand_txt = ""
    for card in hand:
        hand_txt = hand_txt + card + " "
    return hand_txt

def bet_or_fold():
    user_input = input("Bet or Fold? ")
    if user_input.lower() == "bet":
        money = int(input("How much are you betting? "))
        if money < 1:
            money = 1
    else:
        money = 0
    return money

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
        




def main():

    suits = ["\u2661", "\u2662", "\u2660", "\u2663"]
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []
    Bank = 100

    for number in numbers:
        for suit in suits:
            deck.append(number + suit)

    titlecard()

    while True:
        house = []
        player = []
        community_cards = []

        shuffled_deck = shuffle_deck(deck)
        
        
        house, shuffled_deck = deal_cards(shuffled_deck)
        player, shuffled_deck = deal_cards(shuffled_deck)

        show_hands(community_cards, house, player)

        print(bet_or_fold())


        community_cards = shuffled_deck[:3]
        del shuffled_deck[:3]

        show_hands(community_cards, house, player)

        print(bet_or_fold())


        community_cards = community_cards + shuffled_deck[:1]
        del shuffled_deck[:1]
        show_hands(community_cards, house, player)

        print(bet_or_fold())


        community_cards = community_cards + shuffled_deck[:1]
        del shuffled_deck[:1]

        show_hands(community_cards, house, player)

        print(bet_or_fold())
        


        break
        #input("Play? (yes/no): ").split(",")



if __name__ == "__main__":
    main()