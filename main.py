import numpy as np 
import random


from utility.readCsv import readCsv, getVariableObjective
from utility.paretoDetermination import pareto
from utility.plot import plotFitness
from utility.encode_decode import encodeValue,decodeAndGetSolution
from utility.fitness import getFitness
from utility.selectAntibodies import selectFittestAntibodies
from utility.mutation import mutate


df = readCsv("booth.csv")
variables, solutions, minVariable,maxVariable = getVariableObjective(df)


def movingaverage(interval, window_size):
	window = np.ones(int(window_size))/float(window_size)
	return np.convolve(interval, window, 'same')

best_fitness=[]
for i in range(30):
	print('GEN {0}'.format(i+1))
	ND,D,ND_sol,D_sol = pareto(variables,solutions,['min'])
	NDB,DB = encodeValue(ND,20),encodeValue(D,20)

	#print(np.array(NDB).shape,np.array(DB).shape)
	#print(np.array(NDB))
	"""
	NDB : Antigens
	DB  : Antibodies

	For Antigen
	-------------------------------
	w = 4 for   constrained problem
	w = 2 for unconstrained problem 

	Select a random Antigen at random 
	and assign a fitness value to each
	antibodies with respect to this 
	antigen amtching value. 
	"""
	#print('Non dominating set',NDB)
	antigen = random.choice(NDB)
	#print(antigen)

	fitness = np.array(getFitness(DB,antigen,2))
	print('best fitness',max(fitness))
	best_fitness.append(max(fitness))

	"""
	Parameters
	--------------------------------
	antibodies,fitness,q=None,N=None
	"""
	selectedAntibodies = selectFittestAntibodies(DB,fitness,len(variables)-len(D))
	#print(selectedAntibodies[4:8],len(selectedAntibodies))

	mutatedAntibody = mutate(selectedAntibodies,antigen)
	#print(mutatedAntibody[4:8],len(mutatedAntibody))

	decodedArr,nextGenSolution = decodeAndGetSolution(mutatedAntibody,variables,solutions,minVariable,maxVariable)


	#print(nextGenSolution.shape,np.array(D_sol).shape)


	variables = np.concatenate((decodedArr,np.array(D)))
	solutions = np.concatenate((nextGenSolution,np.array(D_sol)))


plotFitness(movingaverage(best_fitness,3)[:-1],"booth.png")