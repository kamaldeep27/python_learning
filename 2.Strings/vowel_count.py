# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'
# in python 2.7
# input Equivalent to eval(raw_input(prompt))
# raw_input: The function reads a line from input, converts it to a string (stripping a trailing newline), and returns that
# from python3 raw_input() is replaced by input()

s = str(raw_input('Enter any string: '))
count = 0
for i in s:
	if i in ['a','e','i','o','u']:
		count += 1
print('vowels in string: ',count)