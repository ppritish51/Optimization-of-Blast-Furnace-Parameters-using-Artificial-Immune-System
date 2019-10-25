import numpy as np

def createPopulation(count=100,bits=10,dimension=1):
	if dimension == 1:
		x = np.random.rand(count,bits)	
		x[x>=0.5] = 1
		x[x< 0.5] = 0

		return np.array([x])
	if dimension==2:
		raise ValueError('Need Implementation')