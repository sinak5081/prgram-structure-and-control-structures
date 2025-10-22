import  math
n = int(input("Enter your number: "))
sum = 0
for i in range(1 , n + 1):
    if(n < 10):
        sum += 1 / (math.factorial(i))
    else:
        print("Enter number >10:")
        break
print(sum)