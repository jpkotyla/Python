from scipy.special import comb
import math
import pandas as pd


def num_arrange(n):
    num_arrange_dict = {0:0}
    for j in range(1,n+1):
        num_arrange_dict[j] = math.factorial(j) - sum([comb(j,i)*num_arrange_dict[i] for i in range(0,j,1)]) - 1
    return num_arrange_dict[n]


derange = pd.Series({i:num_arrange(i) for i in range(1,100)})
factorials = pd.Series({i:math.factorial(i) for i in range(1,100)})

