# Card format - (Number 2-14, Suit 0-3)
# It has been assumed that a higer draw is checked before a lower draw
# Each function returns a list for lexicographic comparison

# 0: High Card
# 1: Pair
# 2: Two Pair
# 3: Three of a Kind
# 4: Straight
# 5: Flush
# 6: Full House
# 7: Four of a Kind
# 8: Straight Flush
# 9: Royal flush *redundant


def getFst(cards):
    return [x[0] for x in cards]

def removeDuplicates(cards):
    return list(set(cards))

def removeAll(cards, val):
    return [x for x in cards if x != val]


# REDUNDANT FUNCTION
# def isRoyalFlush(all_cards):
#     cards = sorted(all_cards, reverse=True, key=lambda x: (x[1], x[0]))  # order by suit then value
#     for i in range(2):
#         if(cards[i][0] == 14 and
#            cards[i+1][0] == 13 and cards[i][1] == cards[i+1][1] and
#            cards[i+2][0] == 12 and cards[i][1] == cards[i+2][1] and
#            cards[i+3][0] == 11 and cards[i][1] == cards[i+3][1] and
#            cards[i+4][0] == 10 and cards[i][1] == cards[i+4][1]):
#             return [9]
#     return isStraightFlush(all_cards)


def isStraightFlush(all_cards):
    cards = sorted(all_cards, reverse=True, key=lambda x: (x[1], x[0]))
    for i in range(len(cards)-4):
        if(cards[i][0] == cards[i+1][0] + 1 and cards[i][1] == cards[i+1][1] and
           cards[i][0] == cards[i+2][0] + 2 and cards[i][1] == cards[i+2][1] and
           cards[i][0] == cards[i+3][0] + 3 and cards[i][1] == cards[i+3][1] and
           cards[i][0] == cards[i+4][0] + 4 and cards[i][1] == cards[i+4][1]):
            return [8] + getFst(cards[i:i+5])
    cards = [((x[0]-1)%13+1, x[1]) for x in cards]  # Change representation of ace from 14 to 1
    cards.sort(reverse=True, key=lambda x: (x[1], x[0]))
    for i in range(len(cards)-4):
        if(cards[i][0] == cards[i+1][0] + 1 and cards[i][1] == cards[i+1][1] and
           cards[i][0] == cards[i+2][0] + 2 and cards[i][1] == cards[i+2][1] and
           cards[i][0] == cards[i+3][0] + 3 and cards[i][1] == cards[i+3][1] and
           cards[i][0] == cards[i+4][0] + 4 and cards[i][1] == cards[i+4][1]):
            return [8] + getFst(cards[i:i+5])
    return isFourOfAKind(all_cards)


def isFourOfAKind(all_cards):
    cards = getFst(all_cards)
    cards.sort(reverse=True)
    for i in range(len(cards)-3):
        if(cards[i] == cards[i+1] and
           cards[i] == cards[i+2] and
           cards[i] == cards[i+3]):
            val = cards[i]
            cards = removeAll(cards, val)
            return [7, val, cards[0]]
    return isFullHouse(all_cards)


def isFullHouse(all_cards):
    cards = getFst(all_cards)
    cards.sort(reverse=True)
    for i in range(len(cards)-2):
        if(cards[i] == cards[i+1] and
           cards[i] == cards[i+2]):
            val1 = cards[i]
            cards = removeAll(cards, val1)
            for j in range(len(cards)-1):
                if(cards[j] == cards[j+1]):
                    val2 = cards[j]
                    cards = removeAll(cards, val2)
                    return [6, val1, val2]
            return isFlush(all_cards)
    return isFlush(all_cards)


def isFlush(all_cards):
    cards = sorted(all_cards, reverse=True, key=lambda x: (x[1], x[0]))
    for i in range(len(cards)-4):
        if(cards[i][1] == cards[i+1][1] and
           cards[i][1] == cards[i+2][1] and
           cards[i][1] == cards[i+3][1] and
           cards[i][1] == cards[i+4][1]):
            return [5] + getFst(cards[i:i+5])
    return isStraight(all_cards)


def isStraight(all_cards):
    cards = removeDuplicates(getFst(all_cards))
    cards.sort(reverse=True)
    for i in range(len(cards)-4):
        if(cards[i] == cards[i+1] + 1 and
           cards[i] == cards[i+2] + 2 and
           cards[i] == cards[i+3] + 3 and
           cards[i] == cards[i+4] + 4):
            return [4] + cards[i:i+5]
    cards = [(x-1)%13+1 for x in cards]  # Change representation of ace from 14 to 1
    cards.sort(reverse=True)
    for i in range(len(cards)-4):
        if(cards[i] == cards[i+1] + 1 and
           cards[i] == cards[i+2] + 2 and
           cards[i] == cards[i+3] + 3 and
           cards[i] == cards[i+4] + 4):
            return [4] + cards[i:i+5]
    return isThreeOfAKind(all_cards)


def isThreeOfAKind(all_cards):
    cards = getFst(all_cards)
    cards.sort(reverse=True)
    for i in range(len(cards)-2):
        if(cards[i] == cards[i+1] and
           cards[i] == cards[i+2]):
            val = cards[i]
            cards = removeAll(cards, val)
            return [3, val, cards[0], cards[1]]
    return isTwoPair(all_cards)


def isTwoPair(all_cards):
    cards = getFst(all_cards)
    cards.sort(reverse=True)
    for i in range(len(cards)-1):
        if(cards[i] == cards[i+1]):
            val1 = cards[i]
            cards = removeAll(cards, val1)
            for j in range(len(cards)-1):
                if(cards[j] == cards[j+1]):
                    val2 = cards[j]
                    cards = removeAll(cards, val2)
                    return [2, val1, val2, cards[0]]
            return isPair(all_cards)
    return isPair(all_cards)


def isPair(all_cards):
    cards = getFst(all_cards)
    cards.sort(reverse=True)
    for i in range(len(cards)-1):
        if(cards[i] == cards[i+1]):
            val = cards[i]
            cards = removeAll(cards, val)
            return [1, val, cards[0], cards[1], cards[2]]
    return isHighCard(all_cards)


def isHighCard(all_cards):
    cards = getFst(all_cards)
    cards.sort(reverse=True)
    return [0] + cards[:5]


def getBest(original_cards):
    return isStraightFlush(original_cards)


def main():
    board_list = input("Enter list of boards cards [(value, suit)]")
    hand_list = input("Enter list of hands cards [(value, suit)]")
    original_cards = board_list + hand_list
    print getBest(original_cards)


def test():
    # Code for testing on linked dataset
    # Note: royal flush detected as a straight flush
    # https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-testing.data

    f = open("poker-hand-testing.data")
    ctr = 0
    for line in f:
        ctr += 1
        d = line.split(',')
        c = [(d[1], d[0]), (d[3], d[2]), (d[5], d[4]), (d[7], d[6]), (d[9], d[8])]
        c = [(int(x[0]), int(x[1])) for x in c]
        c = list(map(lambda c: (14, c[1]) if c[0] is 1 else c, c))
        if (getBest(c)[0] != int(d[10])):
            print ctr, c, getBest(c)[0], d[10]


if __name__ == '__main__':
    test()