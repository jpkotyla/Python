


def fair_value(starting_side,n_sided = 100):
    """
    Function that returns player 1's fair value of a game where
    one player 2 rolls an n_sided(int) dice in order to initiate the
    starting_side(int). The players continue to roll until anyone of there
    rolls is a smaller value than the previous roll. Every roll pays player 1
    $1.
    :param n_sided: The number of sides of the dice.
    :param starting_side: the side that values the game
     from a roll starting on that side (int between 1,n_sided)
    :return: fair value (float)
    """

    fair_val = {n_sided:1./(n_sided-1)}

    if starting_side in fair_val:
        return fair_val[starting_side]
    else:
        for side in range(n_sided-1,starting_side-1,-1):
            fair_val[side] =  fair_val[n_sided]*(1 + sum([fair_val[s]/float(n_sided) for s in fair_val.keys() if s > side]))

    return fair_val[starting_side]


def game_value(n_sided=100):

    return (1./float(n_sided))*sum([fair_value(starting_side=k,n_sided=n_sided) for k in range(1,n_sided+1)])


# P(100) = .01(1+P(100))
#P(100) = (.01)/.99 = 1/99.
#P(99) = ((1+P(99))+(1+P(100)))/100.
#      = (1/.99)((1)+(1+P(100)))/100.

