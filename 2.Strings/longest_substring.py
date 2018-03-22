# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# n the case of ties, print the first substring
# slice string using [start:stop:step]
# string are immutable ( value cannot be modified )

s = str(raw_input('Enter any string: '))
substr = ''
largestr = ''
for i in range(len(s)):
    substr = substr + s[i]
    if i == (len(s)-1) or s[i] > s[i+1]:
        if len(substr) > len(largestr):
            largestr = substr
            substr = ''
print('Longest substring in alphabetical order is: ',largestr)