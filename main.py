import numpy as np 
import random


from utility.readCsv import readCsv, getVariableObjective
from utility.paretoDetermination import pareto
from utility.plot import plotPareto
from utility.encode_decode import encodeValue,decodeAndGetSolution
from utility.fitness import getFitness
from utility.selectAntibodies import selectFittestAntibodies
from utility.mutation import mutate


df = readCsv("data2.csv")
variables, solutions = getVariableObjective(df)



for i in range(10):
	print('GEN {0}'.format(i))
	ND,D,ND_sol,D_sol = pareto(variables,solutions,['min','min'])
	NDB,DB = encodeValue(ND,20),encodeValue(D,20)

	print(np.array(NDB).shape,np.array(DB).shape)
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
	#print(fitness)

	"""
	Parameters
	--------------------------------
	antibodies,fitness,q=None,N=None
	"""
	selectedAntibodies = selectFittestAntibodies(DB,fitness)
	#print(selectedAntibodies[4:8],len(selectedAntibodies))

	mutatedAntibody = mutate(selectedAntibodies,antigen)
	#print(mutatedAntibody[4:8],len(mutatedAntibody))

	decodedArr,nextGenSolution = decodeAndGetSolution(mutatedAntibody,variables,solutions)



	print(decodedArr.shape,np.array(D).shape)


	variables = np.concatenate((decodedArr,np.array(D)))
	solutions = np.concatenate((nextGenSolution,np.array(D_sol)))


