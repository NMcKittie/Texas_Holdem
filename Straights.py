# Duplicates Ace to the lowest number so it can wrap around
def aces_to_ones(hand):
    for card in reversed(hand):
        temp_list = list(card)
        if temp_list[0] == 14:
            temp_list[0] = 1
            hand.append(tuple(temp_list))
        else:
            break
    return sorted(hand)

# handles pairs or 3 of a kinds for the straights function
def duplicate_handler(lst, index):
    prev_suit = (lst[index-2])[1]
    if (lst[index])[0] == (lst[index+2])[0]:
        temp_lst = lst[(index):(index+3)]
        for card in temp_lst:
            if card[1] == prev_suit:
                return card, len(temp_lst)
        return temp_lst[0], len(temp_lst)

    else:
        temp_lst = lst[(index):(index+2)]
        for card in temp_lst:
            if card[1] == prev_suit:
                print(card)
                return card, len(temp_lst)        
        return temp_lst[0], len(temp_lst)

# returns a straight, straight flush or a royal flush
def get_straights(hand, index = 0):
    hand = aces_to_ones(hand)
    nothing_seq = [(0,""),(0,""),(0,""),(0,""),(0,"")]
    flush_seq = []
    high_seq = nothing_seq

    while index < len(hand) -5:
        flush = True
        prev_suit = (hand[index])[1]
        temp_list = []
        first_val = (hand[index])[0]
        count = 0 
        inner_index = index

        while inner_index < len(hand):
            saved_index = inner_index
            iterate = 1
            num = (hand[inner_index])[0]
            cur_suit = (hand[inner_index])[1]

            if inner_index+1 < len(hand):
                if num == (hand[inner_index+1])[0]:
                    card, iterate = duplicate_handler(hand, inner_index)
                    num = card[0]
                    cur_suit = card[1]
                    inner_index = hand.index((num, cur_suit))
                   
            if first_val + count == num:

                if prev_suit != cur_suit:
                    flush = False

                temp_list.append(hand[inner_index])
                inner_index = saved_index
                prev_suit = cur_suit
                count += 1
                if count == 5: 
                    break

                inner_index += iterate

            else:
                flush = False
                temp_list = nothing_seq
                break

        index += 1
        if (high_seq[1])[0] < (temp_list[1])[0]:
            high_seq = temp_list
        elif flush:
            flush_seq = temp_list

    if not flush_seq:
        return (high_seq, "Straight")
    elif high_seq == nothing_seq:
        return None
    else:
        if flush_seq[0][0] == 10 and flush_seq[0][1] == "H":
            return (flush_seq, "Royal_Flush")
        else:
            return (flush_seq, "Straight_Flush")