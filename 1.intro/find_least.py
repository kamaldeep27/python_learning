# 2.Write a program to find least of 3 numbers from user input
print('Find the least')
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
z = int(input('Enter third number: '))
if x < y and x < z :
	print(x,' is least')
elif y < z :
	print(y,' is least')
else :
	print(z,' is least')