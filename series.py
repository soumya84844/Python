n = int(input('Enter number of terms of the series : '))
term  = 1
sum = 0
for i in range(n):
    sum = sum + term
    term = term + 2
print('Sum of the series =',sum)