import matplotlib.pyplot as plt
import numpy as np 


#### [x,y] , x and y are list
def plotPareto(solution,name='pareto.png'):
	
	dimension = len(solution)
	if dimension == 2:
		plt.scatter(solution[0,:],solution[1,:],s=25)
		#plt.plot(solution[0,:],solution[1,:])
		fig = plt.gcf()
		if __name__ == '__main__':
			fig.savefig('./plots/'+name)
		else:
			fig.savefig('./utility/plots/'+name)
	elif dimension == 3:
		pass

#solution = np.array([[0,1],[1,1]])
#plotPareto(solution)
