



def getFitness(antibodies,antigen,W=2):
	n = len(antibodies)
	numVariables = len(antibodies[0])

	final = [0 for i in range(n)]

	for i in range(n):
		temp = 0
		for j in range(numVariables):
			Z = getMatchValue(antibodies[i][j], antigen[j], W)
			temp = temp + Z
		final[i] = temp
	return final


def getMatchValue(a,b,W):
	
	total = 0
	temp = 0
	sum_ =  0
	for i,j in zip(a,b):
		if i == j:
			temp+=1
		else:
			total = total+temp
			sum_ = sum_ + temp**int(W)
			temp = 0
	total = total + temp
	sum_ = sum_ + temp**int(W)
	#print(total,temp,sum_)
	return sum_ + total


#print(getFitness([['111101101'],['101100110'],['101110010']], ['011001110'], '2'))