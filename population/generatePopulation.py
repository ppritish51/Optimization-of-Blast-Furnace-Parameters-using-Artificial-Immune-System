import numpy as np

def createPopulation(bits=10,count=100):

	x = np.random.random(count,bits)	
	x[x>=0.5] = 1
	x[x< 0.5] = 0

	return x