row = int(input('Enter number of rows : '))
term = 1
diff = 3
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(term, end = ' ')
    print()
    term = term + diff
    diff = diff + 2