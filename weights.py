import numpy as np
import math.e as e

def calculateweights(x,a):
	weights=[]
	test=np.linalg.norm(np.array(a))
	for input in x:
		input=np.linalg.norm(np.array(input))
		weights.append(e**(-(test-input)**2))
	return weights