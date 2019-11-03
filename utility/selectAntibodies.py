import numpy as np

def selectFittestAntibodies(antibodies,fitness,q=None,N=None):
	n = len(antibodies)
	numVariables = len(antibodies[0])

	if q==None:
		if n>500:
			q = n//5
		else:
			q = n//2
	temp = fitness.argsort()[-q:][::-1]

	final = [antibodies[i] for i in temp]
	if N ==None:
		if len(final) <250:
			N = 3
		else:
			N = len(final)//200
	return np.array(final*(N) )