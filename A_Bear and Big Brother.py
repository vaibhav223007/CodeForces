limak, bob = [int(x) for x in input().split()]
year = 0

while limak <= bob:
    year += 1
    limak *= 3
    bob *= 2

print(year)
