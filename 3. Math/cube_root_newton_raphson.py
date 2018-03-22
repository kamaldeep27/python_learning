# 8.Find cube root of a number close to accuracy of 0.01 using bisection search algorithm .
# 	handle fractions and negative numbers also. Print number of iteration used to find solution
#	EXTRA: Try using Newton - raphson method to get next guess
num = float(raw_input('Enter any number: '))
g = num/2
h = num
l = 0
i = 0
while num > 1 and abs((g**3) - num) > 0.01:
    if (g**3) > num:
        h = g
    elif (g**3) < num:
        l = g
    g = (l+h)/2
    i+=1
print("got",g," in ",i,"iterations")