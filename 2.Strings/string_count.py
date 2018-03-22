# Write a program that prints the number of times the string 'bob' occurs in string s
s = str(raw_input('Enter any string: '))
substr = 'bob'
count = 0
for i in range(0,len(s)):
	if s[i:i+3] == 'bob':
		count += 1
print('Number of times bob occurs is: ',count)