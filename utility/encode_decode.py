from scipy import spatial
import numpy as np 

#[[element,element,..],[element,element,..]]
def encodeValue(arr,bits=8):
	n = len(arr)
	numVariables = len(arr[0])

	final = [[0]*numVariables for i in range(n)]

	for i in range(n):
		for j in range(numVariables):
			if arr[i][j] < 0:
				final[i][j] = bin(((1 << bits) - 1) & int(arr[i][j]))[2:]
			else:
				final[i][j] = bin(int(arr[i][j]))[2:].zfill(bits)

	return final



def getTwoNearestPointIndices(arr,variables,solutions):
	tree = spatial.KDTree(variables)
	return tree.query(arr,k=2)[1]

def getSolution(arr,variables,solutions,IndexOfSolutionToChoose,n,numSolutions):
	final = [0 for i in range(n)]

	for i,j in zip(IndexOfSolutionToChoose,range(n)):
		final[j] = (solutions[i[0]]+ solutions[i[1]])//2

	return final


def decodeAndGetSolution(arr,variables,solutions,minVariable,maxVariable):

	n = len(arr)
	numVariables = len(arr[0])
	numSolutions = len(solutions[0])


	decodedArr = decode(arr,n,numVariables)
	IndexOfSolutionToChoose = getTwoNearestPointIndices(decodedArr, variables, solutions)

	nextGenSolution = getSolution(arr, variables, solutions,IndexOfSolutionToChoose, n,numSolutions)
	"""finaldecodedArr = []
	finalNextGenSOlutions = []

	for i,z in zip(decodedArr,nextGenSolution):
		flag = True
		for j in range(len(i)):
			if not minVariable[j]<=i[j]<=maxVariable[j]:
				flag = False
		if flag:	
			finaldecodedArr.append(i)
			finalNextGenSOlutions.append(z)

	print('fsafgas',np.array(finaldecodedArr).shape,np.array(finaldecodedArr*len(variables[0])).shape)
	return np.array(finaldecodedArr*(len(variables)//len(finaldecodedArr) )),np.array(finalNextGenSOlutions * (len(variables)//len(finaldecodedArr) ))"""
	return  np.array(decodedArr),np.array(nextGenSolution)


def decode(arr,n,numVariables):

	final = [[0]*numVariables for i in range(n)]

	for i in range(n):
		for j in range(numVariables):
			final[i][j] = int(arr[i][j],2)

	return final


#print(encodeValue([[1,2,3],[4,5,6]]))
