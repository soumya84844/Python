num1 = float(input("Enter the first num : "))
num2 = float(input("Enter the second num : "))
op = input("Enter operator[+ - * / %] : ")
result = 0
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1/num2
elif op == '%':
    result = num1 % num2
else:
    print("Invalid operator")
    exit()
print(str(num1) + op + str(num2) + "=" + str(result))