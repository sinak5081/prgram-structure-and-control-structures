text = input("Enter your alphanumric string: ")
count = 0
for char in text:
    if char >= "0" and char <= "9":
        count += 1
        print(char,end = " ")
print("\n number of digit is : ", count)