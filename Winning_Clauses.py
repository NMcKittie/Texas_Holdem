
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


# Checks if the hand is a straight by checking if the numbers are in sequence
def check_sequence(a_dict):
    a_dict = a_dict[0]
    print(a_dict)
    mykeys = list(a_dict.keys())

    mykeys.sort()

    
    first_val = mykeys[0]
    i = 0
    high_seq = [0,0,0,0,0]

    while i < len(mykeys) - 4:
        temp_list = []
        first_val = mykeys[i]
        print("First_val " + str(first_val))
        #print(first_val)
       # first_val = first_val[0]
        count = 0
        k = i
        while True:
            num = mykeys[k]
            print("index " + str(num))
            if first_val + count == num:
                temp_list.append(num)
                count += 1
                if count == 5: 
                    break
                k += 1
            else:
                temp_list = [0,0,0,0,0]
                break
        i += 1
        #print(count)
        if max(high_seq) < max(temp_list):
            high_seq = temp_list
    
    return high_seq


# Creates a tuple with 2 dictionaries inside, one counts the number of times a card value occurs. The other dict counts the number of times a suit occurs
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


tup = count_cards(["2H", "3S", "4S", "5D", "6S", "2D", "8H", "9K", "10P", "11K", "12P"])
print(tup)
print(check_sequence(count_cards))