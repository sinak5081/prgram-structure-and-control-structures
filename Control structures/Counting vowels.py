string = input("Enter a string: ")
sound = "aAeEiIuUoO"
count = 0
for char in string:
    if char in sound:
        count += 1
print("count of sound letters is: ",count)