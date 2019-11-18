import matplotlib.pyplot as plt
import numpy as np 


#### [x,y] , x and y are list
def plotFitness(fitness,name='fitness.png'):
	

	plt.plot(fitness)
	#plt.plot(solution[0,:],solution[1,:])
	fig = plt.gcf()
	if __name__ == '__main__':
		fig.savefig('./plots/'+name)
	else:
		fig.savefig('./utility/plots/'+name)

#solution = np.array([[0,1],[1,1]])
#plotPareto(solution)
