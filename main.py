import numpy as np 

from utility.decodedValue import decodeValue
from utility.paretoDetermination import pareto
from dummy.dummyFunction import schaffer 


population = np.array([[[1,0,1,0,0,1,1,0],[1,0,0,0,0,0,1,1,1]]])
lowerLimit, upperLimit = np.array([-20]), np.array([20])
data = decodeValue(population, lowerLimit, upperLimit)
print('data',data)
output = schaffer(data)
print('output',output)
print(pareto(population,data,output,2,['min','min'],lowerLimit, upperLimit))





