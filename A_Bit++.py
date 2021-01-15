number = int(input())
initial_number = 0

for i in range(number):
    operation = input()
    if "++" in operation:
        initial_number += 1
    else:
        initial_number -= 1

print(initial_number)

