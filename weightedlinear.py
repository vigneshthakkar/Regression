from weights import calculateweights
from sklearn import linear_model

def weightedlinearregression():
	print('Enter the number of data points : ')
	points=int(input())
	x,y=[],[]
	for i in range(points):
		print('For point '+(i+1)+' enter the feature vector : ')
		a=[float(number) for number in input().split()]
		x.append(a)
		print('For point '+(i+1)+' enter the output vector : ')
		a=[float(number) for number in input().split()]
		y.append(a)
	ch='y'
	while ch=='y':
		print('Enter the test vector : ')
		a=[[float(number) for number in input().split()]]
		weights=calculateweights()
		lr=linear_model.LinearRegression()
		lr.fit(x,y,sample_weights=weights)
		y=lr.predict(a)
		for output in y:
			print('The predicted value for the given test vector is : ')
			print(output)
		print('Test another input? (y/n) ')
		ch=input()