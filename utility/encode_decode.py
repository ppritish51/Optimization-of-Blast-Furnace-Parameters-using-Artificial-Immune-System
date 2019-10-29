

#[[element,element,..],[element,element,..]]
def encodeValue(arr,bits=8):
	n = len(arr)
	numVariables = len(arr[0])

	final = [[0]*numVariables for i in range(n)]

	for i in range(n):
		for j in range(numVariables):
			if arr[i][j] < 0:
				final[i][j] = bin(((1 << bits) - 1) & arr[i][j])[2:]
			else:
				final[i][j] = bin(arr[i][j])[2:].zfill(bits)

	return final











#print(encodeValue([[1,2,3],[4,5,6]]))
