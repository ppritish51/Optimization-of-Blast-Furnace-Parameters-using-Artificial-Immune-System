import numpy as np 

from utility.decodedValue import decodeValue
from utility.paretoDetermination import pareto
from dummy.dummyFunction import schaffer 
from utility.plot import plotPareto
from population.generatePopulation import createPopulation


#### [x,y] , x and y are list
population = createPopulation(10,8,1) #np.array([[[1,0,1,0,0,1,1,0],[1,0,0,0,0,0,1,1,1]]])
print(population)
lowerLimit, upperLimit = np.array([-20]), np.array([20])
data = decodeValue(population, lowerLimit, upperLimit)
print('data',data)
output = schaffer(data)
print('output',output)
plotPareto(output,'test3.png')
print(pareto(population,data,output,2,['min','min'],lowerLimit, upperLimit))





