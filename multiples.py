nums = list(map(int, input('Enter 5 numbers separated by commas : ').split(',')))
divisor = int(input('Enter divisor : '))
print('Multiples are : ')
for num in nums:
    if(num % divisor == 0):
        print(num)