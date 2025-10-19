num = int(input("Enter a number:(0 to end):"))
sum_cubes = 0
while num != 0:
    num = int(input("Enter a number:"))
    sum_cubes += (num ** 2)
print("sum of cubes : ",sum_cubes)