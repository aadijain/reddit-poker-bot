import logging
from sanitize import validate
from random import randint


# Simulates 1000 draw sample space.
def main(cards):

    dec = gen_dec()
    sample_space = list()
    for i in range(0,1000):
        sample_space.append(simulate(validate(cards), dec))


# selects cards randomly to complete the draw
def simulate(draw, dec):

    player2 = list()

    board_len = draw[0].__len__()

    sim_num = 5-board_len

    # remove cards in hand from dec
    dec.remove(draw[1][0])
    dec.remove(draw[1][0])

    # remove card in board from dec
    for i in range(0, draw[0].__len__()):
        dec.remove(draw[0][i])

    # add random cards to complete the board
    for j in range(0, sim_num):
        rand_int = rand_int(0,dec.__len__())
        draw[0].append(dec[rand_int])
        del dec[rand_int:rand_int + 1]

    # add random cards for to simulate player 2
    for j in range (0, 2):
        player2.append(dec[randint(0, dec.__len__())])

    # add board cards back to the dec
    draw_len = draw[0].__len__()
    for j in range(0, sim_num):
        dec.append(draw[0][draw_len])
        draw_len -= 1

    # add player 2 cards to the dec
    dec.append(player2[0])
    dec.append(player2[1])

    # return draw and 2 players data as a collection of tuples.
    return draw[0], draw[1], player2


# Generates a list of dec of cards
def gen_dec():

    dec = list()
    for i in (0,3):
        for j in range(2,14):
            dec.append(j,i)

    return dec
