num = int(input("Enter your number:"))
sum = 0
hlp = num
while hlp != 0:
    sum += hlp % 10
    hlp = hlp // 10
print("number is :",num , "sum of numbers: ",sum)