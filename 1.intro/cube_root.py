# 3.Write a program to find cube root of a number.handle negative numbers also
x = int(input('x: '))
cuberoot = 0
while cuberoot**3 < abs(x):
	cuberoot += 1
if cuberoot**3 == abs(x):
	if x < 0:
		cuberoot = - cuberoot
	print('cuberoot of ',x,'is',cuberoot)
else:
   print(x,'is not a perfect cube')