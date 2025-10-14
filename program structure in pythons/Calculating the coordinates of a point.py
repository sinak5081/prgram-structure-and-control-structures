import math
x = int(input("Enter a x: "))
y =int(input("Enter a y: "))
x2 = int(input("Enter a x2: "))
y2 = int(input("Enter a y2: "))
d = math.sqrt(math.pow((x2-x), 2)+math.pow((y2 - y), 2))
print("distance is :",format(d))