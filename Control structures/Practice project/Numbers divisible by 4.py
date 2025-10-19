sum = 0
for i in range(10):
    num = int(input("Enter a number: "))
    if(num % 4 == 0):
        sum += 1
print("result of sum: ",sum)