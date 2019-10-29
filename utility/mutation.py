import random

def mutate(antibodies,antigen):
	numVariables  = len(antibodies[0])
	n = len(antibodies)

	final = [[0]*numVariables for i in range(n)]

	for i in range(n):
		for j in range(numVariables):
			final[i][j] = crossover(antibodies[i][j], antigen[j])

	return final

def crossover(antibody,antigen):

	while True:
		a = random.randint(0,len(antibody[0]))
		b = random.randint(0,len(antibody[0]))
		if a!=b:
			if a>b:
				a,b = b,a
			break
	return mutation(antibody[:a]+antigen[a:b]+antibody[b:])	

def mutation(antibody):
	while True:
		pass
		a = random.randint(0,len(antibody[0]))
		b = random.randint(0,len(antibody[0]))
		if a!=b:
			break
	return swap(antibody, a, b)

def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)







