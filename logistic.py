from sklearn import linear_model

def logisticregression():
	print('Enter the number of data points : ')
	points=int(input())
	x,y=[],[]
	for i in range(points):
		print('For point '+str(i+1)+' enter the feature vector : ')
		a=[float(number) for number in input().split()]
		x.append(a)
		print('For point '+str(i+1)+' enter the output integer class : ')
		a=[int(number) for number in input().split()]
		y.append(a)
	lr=linear_model.LogisticRegression(solver='sag')
	lr.fit(x,y)
	ch='y'
	while ch=='y':
		print('Enter the test vector : ')
		a=[[float(number) for number in input().split()]]
		y=lr.predict(a)
		for output in y:
			print('The predicted value for the given test vector is : ')
			print(output)
		print('Test another input? (y/n) ')
		ch=input()
