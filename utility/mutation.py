import random
import numpy as np


def mutate(antibodies,antigen):
	numVariables  = len(antibodies[0])
	n = len(antibodies)

	final = [[0 for j in range(numVariables)] for i in range(n)]
	#print(final)

	for i in range(n):
		for j in range(numVariables):
			final[i][j] = crossover(antibodies[i][j], antigen[j])
		#print(final[:5])

	return np.array(final)

def crossover(antibody,antigen):

	while True:
		#print(len(antibody[0]))
		a = random.SystemRandom().randint(0, len(antibody)-1) 
		b = random.SystemRandom().randint(0, len(antibody)-1)
		if a!=b:
			if a>b:
				a,b = b,a
			break
	#print(a,b)

	return mutation(antibody[:a]+antigen[a:b]+antibody[b:])	

def mutation(antibody):
	while True:
		pass
		a = random.SystemRandom().randint(0, len(antibody)-1) 
		b = random.SystemRandom().randint(0, len(antibody)-1)
		if a!=b:
			break
	return swap(antibody, a, b)

def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)







