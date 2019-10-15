import numpy as np

def createPopulation(count=100):

	x = np.random.random(count,10)	
	x[x>=0.5] = 1
	x[x< 0.5] = 0

	return x