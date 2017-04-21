import time

poss = {1:[6,8],2:[7,9],
		3:[4,8],4:[3,9,0],
		5:[],6:[1,7,0],
		7:[2,6],8:[1,3],
		9:[2,4],0:[4,6]}


def paths(s,n):
    if n == 1:
    	res = len(poss[s])
	else:
	    res = sum([paths(start, n-1) for start in poss[s]])
	return res

def paths_dp(s,n):
	if(n == 1):
		return len(poss[s])
	else:
		import numpy as np
		p = np.zeros(shape = (n,10))
		p[0] = [len(poss[key]) for key in poss.keys()]
		move = 1
		while(move < n):
			for i in range(0,10):
				p[move,i] = sum([p[(move - 1),num] for num in poss[i]])
			move += 1
		return p[(n-1),s]


rec = [time_a(paths,i) for i in range(1,20)]
dp = [time_a(paths_dp,i) for i in range(1,20)]
import matplotlib.pyplot as plt 
plt.plot(range(1,10),rec,'b-')
plt.plot(range(1,10),dp,'r-')
plt.show()