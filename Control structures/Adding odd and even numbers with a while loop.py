sum_even = 0
sum_odd = 0
while True:
    number = int(input("Enter a number: (0 to end): "))
    if number == 0:
        break
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd +=number
print("sum of even: ",sum_even)
print("sum of odd: ",sum_odd)