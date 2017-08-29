# Card format - (Number 2-14, Suit 0-3)
# It has been assumed that a higer draw is checked before a lower draw

def getFst(cards):
    return list(map(lambda x: x, cards))

def removeDuplicates(cards):
    return list(set(cards))

def removeAll(cards, val):
    return [x for x in cards if x != val]

def isRoyalFlush(cards):
    cards.sort(reverse=True, key=lambda x: (x[1], x[0])) #order by suit then value
    for i in range(2):
        if(cards[i][0] == 14 and
           cards[i+1][0] == 13 and cards[i][1] == cards[i+1][1] and
           cards[i+2][0] == 12 and cards[i][1] == cards[i+2][1] and
           cards[i+3][0] == 11 and cards[i][1] == cards[i+3][1] and
           cards[i+4][0] == 10 and cards[i][1] == cards[i+4][1]):
            return [1]
    return None

def isStraightFlush(cards):
    cards.sort(reverse=True, key=lambda x: (x[1], x[0]))
    for i in range(2):
        if(cards[i][0] == cards[i+1][0] + 1 and cards[i][1] == cards[i+1][1] and
           cards[i][0] == cards[i+2][0] + 2 and cards[i][1] == cards[i+2][1] and
           cards[i][0] == cards[i+3][0] + 3 and cards[i][1] == cards[i+3][1] and
           cards[i][0] == cards[i+4][0] + 4 and cards[i][1] == cards[i+4][1]):
            return getFst(cards[i:i+5])
    cards = [((x[0]-1)%13+1, x[1]) for x in cards] #Change representation of ace from 14 to 1
    cards.sort(reverse=True, key=lambda x: (x[1], x[0]))
    for i in range(2):
        if(cards[i][0] == cards[i+1][0] + 1 and cards[i][1] == cards[i+1][1] and
           cards[i][0] == cards[i+2][0] + 2 and cards[i][1] == cards[i+2][1] and
           cards[i][0] == cards[i+3][0] + 3 and cards[i][1] == cards[i+3][1] and
           cards[i][0] == cards[i+4][0] + 4 and cards[i][1] == cards[i+4][1]):
            return getFst(cards[i:i+5])
    return None

def isFourOfAKind(cards):
    cards = getFst(cards)
    cards.sort(reverse=True)
    for i in range(len(cards)-3):
        if(cards[i] == cards[i+1] and
           cards[i] == cards[i+2] and
           cards[i] == cards[i+3]):
            val = cards[i]
            cards = removeAll(cards, val)
            return [val, cards[0]]
    return None

def isFullHouse(cards):
    cards = getFst(cards)
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
                    return [val1, val2]
    return None

def isFlush(cards):
    cards.sort(reverse=True, key=lambda x: (x[1], x[0]))
    for i in range(2):
        if(cards[i][1] == cards[i+1][1] and
           cards[i][1] == cards[i+2][1] and
           cards[i][1] == cards[i+3][1] and
           cards[i][1] == cards[i+4][1]):
            return getFst(cards[i:i+5])
    return None

def isStraight(cards):
    cards = removeDuplicates(getFst(cards))
    cards.sort(reverse=True)
    for i in range(len(cards)-4):
        if(cards[i] == cards[i+1] + 1 and
           cards[i] == cards[i+2] + 2 and
           cards[i] == cards[i+3] + 3 and
           cards[i] == cards[i+4] + 4):
            return cards[i:i+5]
    cards = [((x[0]-1)%13+1, x[1]) for x in cards] #Change representation of ace from 14 to 1
    cards.sort(reverse=True)
    for i in range(len(cards)-4):
        if(cards[i] == cards[i+1] + 1 and
           cards[i] == cards[i+2] + 2 and
           cards[i] == cards[i+3] + 3 and
           cards[i] == cards[i+4] + 4):
            return cards[i:i+5]
    return None

def isThreeOfAKind(cards):
    cards = getFst(cards)
    cards.sort(reverse=True)
    for i in range(len(cards)-2):
        if(cards[i] == cards[i+1] and
           cards[i] == cards[i+2]):
            val = cards[i]
            cards = removeAll(cards, val)
            return [val, cards[0], cards[1]]
    return None

def isTwoPair(cards):
    cards = getFst(cards)
    cards.sort(reverse=True)
    for i in range(len(cards)-1):
        if(cards[i] == cards[i+1]):
            val1 = cards[i]
            cards = removeAll(cards, val1)
            for j in range(len(cards)-1):
                if(cards[j] == cards[j+1]):
                    val2 = cards[j]
                    cards = removeAll(cards, val2)
                    return [val1, val2, cards[0]]
    return None

def isPair(cards):
    cards = getFst(cards)
    cards.sort(reverse=True)
    for i in range(len(cards)-1):
        if(cards[i] == cards[i+1]):
            val = cards[i]
            cards = removeAll(cards, val)
            return [val, cards[0], cards[1], cards[2]]
    return None
