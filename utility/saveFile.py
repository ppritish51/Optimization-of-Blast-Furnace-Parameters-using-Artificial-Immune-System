import pandas as pd 



def save(variables,solutions,name="final.csv"):
	numObjectives = len(solutions[0])
	numVariables  = len(variables[0])


	df = pd.DataFrame()

	for i in range(numVariables):
		df['var'+str(i+1)] = variables[:,i]

	for i in range(numObjectives):
		df['obj'+str(i+1)] = solutions[:,i]

	if __name__ == '__main__':
		df.to_csv('./outputFile/'+name)
	else:
		df.to_csv('./utility/outputFile/'+name)