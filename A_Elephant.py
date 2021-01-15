import math

coordinate = int(input())

step1 = math.floor(coordinate/5)

if coordinate % 5 == 0:
    step1 = coordinate/5
    print(int(step1))

else:
    step1 = math.floor(coordinate/5)
    print(step1 + 1)
