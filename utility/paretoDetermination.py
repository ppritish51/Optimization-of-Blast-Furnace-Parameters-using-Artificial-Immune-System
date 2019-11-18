import numpy as np 


#page 28,29,35
def pareto(variables,solutions,objectives):
	
	"""
	ND: non dominated
	D : dominated
	"""
	
	numObjectives = len(solutions[0])
	numVariables  = len(variables[0])

	ND  = []
	D   = []
	D_sol  = []
	ND_sol = [] 

	n = len(variables)
	for i in range(n):
		flag = False
		for j in range(n):
			if i ==j:
				continue
			temp = compare(solutions[j], solutions[i], numObjectives, objectives)
			#print(solutions[j],solutions[i],objectives)
			if temp:
				#print('got Dominated')
				flag = True
				break
		if flag:
			pass
		else:
			ND.append(variables[i])
			ND_sol.append(solutions[i])

	ND = np.array(ND)

	for i,j in zip(variables,solutions):
		if i in ND:
			pass
		else:
			D.append(i)
			D_sol.append(j)

	return ND,np.array(D),ND_sol,D_sol






#([integer],[integer],integer,[string])
def compare(sol,sol_,numObjectives,objectives):	
	flag = False
	for i,obj in zip(range(numObjectives),objectives):	
		temp = comObjective(sol[i], sol_[i], obj)
		if  temp!=0:
			if temp == 2:
				flag = True			
		else:
			return False

	return flag
	



#(interger,interger,string)
#return 0 => not satisfied
#return 1 => satisfied
#return 2 => satisfied and strictly better than solution
def comObjective(sol,sol_,objective):
	#print(sol,sol_,objective)
	if objective == 'min':
		if sol < sol_:
			#print(2)
			return 2
		if sol == sol_:
			#print(1)
			return 1
		else:
			#print(0)
			return 0
	elif objective == 'max':
		if sol > sol_:
			return 2
		if sol == sol_:
			return 1
		else:
			return 0
			




#print(pareto([[1],[2],[3],[4],[5]],[[9,2],[8,5],[12,1],[11,3],[16,2]],['max','min']))
#print(pareto([[-10,10],[-20,0],[0,20],[10,30]], [[100,64],[0,4],[400,324],[900,784]],['min','min']))






