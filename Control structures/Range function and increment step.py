x = int(input("Enter your number for x: "))
n = int(input("Enter your number for N: "))
sum = 0
sign = 1
for i in range(1,n + 1,2):
    sum = sum + (x ** i) * sign
    sign = -sign
print("sum : ",sum)    


#equation is: x**1 - x**3 + x**5 - ............ + x**n 
