import numpy as np

def selectFittestAntibodies(antibodies,fitness,q=None,N=None):
	n = len(antibodies)
	numVariables = len(antibodies[0])

	if q==None:
		q = int(n/2)
	temp = fitness.argsort()[-q:][::-1]

	final = [antibodies[i] for i in temp]
	if N ==None:
		N = 5
	return np.array(final*N )