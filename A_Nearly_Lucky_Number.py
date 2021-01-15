number = int(input())
count = 0

for digit in str(number):
    if int(digit) == 4 or int(digit) == 7:
        count += 1

if count == 4 or count == 7:
    print('YES')
else:
    print('NO')
