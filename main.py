import numpy as np 

from utility.decodedValue import decodeValue
from dummy.dummyFunction import schaffer 


population = [[1,0,1,0,0,1,1,0],[1,0,0,0,0,0,1,1,1]]
x = decodeValue(population,-20,20)
print('x',x)
print(schaffer(x))