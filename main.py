import numpy as np 
import random


from utility.readCsv import readCsv, getVariableObjective
from utility.paretoDetermination import pareto
from utility.plot import plotPareto
from utility.encode_decode import encodeValue
from utility.fitness import getFitness
from utility.selectAntibodies import selectFittestAntibodies
from utility.mutation import mutate


df = readCsv()
variables, solutions = getVariableObjective(df)
ND,D = pareto(variables,solutions,['min','min'])
NDB,DB = encodeValue(ND),encodeValue(D)

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
print(selectedAntibodies[0],len(selectedAntibodies))

mutatedAntibody = mutate(selectedAntibodies,antigen)
print(mutatedAntibody[0],len(mutatedAntibody))


