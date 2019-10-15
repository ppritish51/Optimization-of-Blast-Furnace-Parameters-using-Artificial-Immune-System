import numpy as np 

from utility.decodedValue import decodeValue
from dummy.dummyFunction import schaffer 


population = np.array([[[1,0,1,0,0,1,1,0],[1,0,0,0,0,0,1,1,1]]])
x = decodeValue(population, np.array([-20]), np.array([20]))
print('x',x)
print(schaffer(x))