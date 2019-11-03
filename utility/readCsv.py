import pandas as pd 


def readCsv(filename):
	if __name__ == '__main__':
		df = pd.read_csv('../data/'+filename)
	else:
		df = pd.read_csv('./data/'+filename)

	return df 

def getVariableObjective(df):
	cols = df.columns
	variables  = df[[col for col in cols if 'y' in col]].values
	objectives = df[[col for col in cols if 'f' in col]].values

	return variables,objectives










