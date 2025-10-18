number1 = int(input("Enter number: (0 to end):"))
sumsq = 0
while number1 != 0:
    sumsq += number1 ** 2
    number1 = int(input("Enter number: (0 to end):"))
print("sum of squares is: ",sumsq)