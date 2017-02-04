from linear import linearregression
from weightedlinear import weightedlinearregression
from logistic import logisticregression

char='y'
while char=='y':
	print('Chose from one of the following : ')
	print('1. Linear Regression')
	print('2. Weighted Linear Regression')
	print('3. Logistic Regression')
	print('Enter your choice : ')
	choice=int(input())
	if choice==1: linearegression()
	elif choice==2: weightedlinearegression()
	elif choice==3: logisticregression() 
	print('What to do another regression? (y/n)')
	char=input()
