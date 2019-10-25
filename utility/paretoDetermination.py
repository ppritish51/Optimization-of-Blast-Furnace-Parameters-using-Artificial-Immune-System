import numpy as np 

def pareto(population,variables,solutions,numObjectives=1,objectives=['min'],lowerLimit=None,upperLimit=None):
	
	"""
	NDF: non dominated feasible
	DF : dominated feasible
	DNF: dominated non feasible
	NDNF: non dominated non feasible
	"""
	
	dimension = len(population)

	NDF  = [np.array([]) for i in range(dimension)]
	DF   = [np.array([]) for i in range(dimension)]
	DNF  = [np.array([]) for i in range(dimension)]
	NDNF = [np.array([]) for i in range(dimension)] 

	n = len(solutions)
	for i in range(n):
		for j in range(n):
			if i ==j:
				continue
			




	







