import numpy as np  

def decodeValue(population,lowerBound,upperBound):
	temp = []

	for member in population:
		l = len(member)
		val = 0
		ind = 0
		for ii in member[::-1]:
			val = val + (2**ind)*ii
			ind = ind + 1
		
		val  = lowerBound + (((upperBound - lowerBound) / (2**l -1)) * val) 
		temp.append(val)

	return np.asarray((temp))


population = [[1,0,1,0,0,1,1,0],[1,0,0,0,0,0,1,1,1]]
print(decodeValue(population, -20, 20))






