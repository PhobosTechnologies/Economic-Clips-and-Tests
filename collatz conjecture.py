num = int(input("Enter starting number: "))

while num != 1:
    print(num)
    if num%2 == 0:
        num = num/2
        # print(num)
    else:
        num = num*3+1
        # print(num)

print(num)