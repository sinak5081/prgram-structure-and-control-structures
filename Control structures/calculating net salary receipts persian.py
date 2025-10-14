salary = int(input("Enter your salary of the month(تومان): "))
if salary < 2000000:
    taxes = salary * 0.00
elif salary < 3000000:
    taxes = salary * 0.02
elif salary < 5000000:
    taxes = salary * 0.03
else:
    taxes = salary * 0.10
print("taxes is: ",taxes)
print("net income:",salary - taxes)