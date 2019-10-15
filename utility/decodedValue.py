import numpy as np  

def decodeValue(population,lowerBound,upperBound):
	dimension = len(population)
	#print(dimension)
	temp = [np.array([]) for i in range(dimension)]
	#print(temp)

	for i in range(dimension):
		#print(i)
		for member in population[i,:]:
			l = len(member)
			val = 0
			ind = 0
			for ii in member[::-1]:
				val = val + (2**ind)*ii
				ind = ind + 1
			
			val  = lowerBound[i] + (((upperBound[i] - lowerBound[i]) / (2**l -1)) * val) 
			#print(member,' : ',val)
			temp[i] = np.append(temp[i],val)
			
	return np.asarray(temp)

#### [x,y] , x and y are list
##population = np.array([[[1,0,1,0,0,1,1,0],[1,0,0,0,0,0,1,1,1]]])
##print(decodeValue(population, np.array([-20]), np.array([20])))

##population = np.array([[[1,0,1,0,0,1,1,0],[1,0,0,0,0,0,1,1,1]],[[1,0,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,0]]])
##print(decodeValue(population, np.array([-20,0]), np.array([20,10])))




