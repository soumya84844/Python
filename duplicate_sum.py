a = int(input('Enter the 1st number : '))
b = int(input('Enter the 2nd number : '))
c = int(input('Enter the 3rd number : '))
sum1 = a + b + c
print("Sum1 = ", sum1)
sum2 = 0
if(a == b == c):
    sum2 = 0
elif(a == c):
    sum2 = b
elif(a == b):
    sum2 = c
elif(b == c):
    sum2 = a
else:
    sum2 = sum1
print("Sum2 = ", sum2)