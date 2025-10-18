done = True
odd = 0
while done:
    num = int(input("Enter a number:"))
    if num % 2 == 0:
        print("number is even , Enter a odd number:")
        continue
    odd += num
    ans = input("Do you want to continue (y/f):")
    if ans == "y"or ans == "Y":
        continue
    done = False
    print("sum of odd numbers ",odd)

         