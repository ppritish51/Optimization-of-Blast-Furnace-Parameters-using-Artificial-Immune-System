import numpy as np 


#minimize f1 and f2
#-20<x<20
def schaffer(decisionVariable):

	x = decisionVariable[0]
	return np.asarray([x**2,(x-2)**2])


#print(schaffer(np.array([[1,2,3,4,5,6]])))