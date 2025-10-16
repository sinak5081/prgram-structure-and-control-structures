sum_even = 0
sum_odd = 0
for i in range(1,101):
    if(i%2==0):
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i
print("even is:",sum_even)
print("odd is: ",sum_odd)
