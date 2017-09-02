def validate(cards):

    cards.lower()
    cards.strip()

    # check formatting
    try:
        board_count = cards.index(' ')
    except Exception as e:
        return None, "Input format error, no space found!", e

    board = cards[:board_count]
    hand = cards[board_count + 1:]

    # check for flop and 2 card hand
    if board.__len__() < 6:
        return None, "Pre-flop data not accepted!", board
    elif board.__len__() > 10:
        return None, "Greater than 5 cards on board!", board
    if hand.__len__() != 4:
        return None, "Hand information error!", hand

    # check for duplicate card entry
    temp_hand = board + hand
    for i in range(0, temp_hand.__len__() - 2, 2):
        card1 = temp_hand[i] + temp_hand[i + 1]
        for j in range(i + 2, temp_hand.__len__(), 2):
            card2 = temp_hand[j] + temp_hand[j + 1]
            if card1 == card2:
                return None, "Repeated card!", card1

    board_list = convert(board)
    hand_list = convert(hand)

    return board_list, hand_list


def convert(cards):
    card = list()

    for i in range(0, cards.__len__(), 2):

        value = cards[i]
        suite = cards[i + 1]

        if value == '1' or value == 'a':
            value = 14
        elif value == 't':
            value = 10
        elif value == 'j':
            value = 11
        elif value == 'q':
            value = 12
        elif value == 'k':
            value = 13
        else:
            value = int(value)

        if suite == 's':
            suite = 0
        elif suite == 'h':
            suite = 1
        elif suite == 'c':
            suite = 2
        elif suite == 'd':
            suite = 3

        card.append((value, suite))

    return card
