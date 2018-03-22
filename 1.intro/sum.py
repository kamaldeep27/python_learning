# 4.Write a while loop that sums the values 1 through end, inclusive. End is int variable from user input
end = int(input("Enter an integer: "))
i = 0
num = 0
while True:
    num += i
    i += 1
    if i > end:
        break
print(num)