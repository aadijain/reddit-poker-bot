from sanitize import validate
from random import randint
from priority import getBest

wins = [0,0,0]


# Simulates 1000 draw (default) and calculates winning odds
def main(cards, monte_count=1000):

    dec = gen_dec()
    global wins
    wins = [0, 0, 0]

    for i in range(0, monte_count):
        result(simulate(cards, dec))

    # return winning probability
    # return wins[1]*1.0 / monte_count
    return wins


# Calls getBest() abd updates winning hand
def result(cards):

    p1 = getBest(cards[0] + cards[1])
    p2 = getBest(cards[0] + cards[2])

    if p1 > p2:
        wins[1] += 1
    elif p2 > p1:
        wins[2] += 1
    else:
        wins[0] += 1


# selects cards randomly to complete the draw
def simulate(draw, dec):

    player2 = list()
    board_len = draw[0].__len__()
    sim_num = 5-board_len

    # remove cards in hand from dec
    dec.remove(draw[1][0])
    dec.remove(draw[1][1])

    # remove card in board from dec
    for i in range(0, draw[0].__len__()):
        dec.remove(draw[0][i])

    # add random cards to complete the board
    for j in range(0, sim_num):
        rand_int = randint(0, dec.__len__() - 1)
        draw[0].append(dec[rand_int])
        del dec[rand_int:rand_int + 1]

    # add random cards for to simulate player 2
    for j in range(0, 2):
        rand_int = randint(0, dec.__len__() - 1)
        player2.append(dec[rand_int])
        del dec[rand_int:rand_int + 1]

    # add board cards back to the dec
    for j in range(0, draw[0].__len__()):
        dec.append(draw[0][j])

    # add player 2 cards to the dec
    dec.append(player2[0])
    dec.append(player2[1])
    dec.append(draw[1][0])
    dec.append(draw[1][1])
    if sorted(dec) != sorted(gen_dec()):
        print "!!!!!!!!!!ERRORRR!!!!!!"
    # return draw and 2 players data as a collection of tuples.
    return draw[0], draw[1], player2


# Generates a list of dec of cards
def gen_dec():

    dec = list()
    for i in range(0, 4):
        for j in range(2, 15):
            dec.append((j, i))

    return dec

# Tester function call
print main(validate("1h2h3h4h5s 4c5c"), 10000)
