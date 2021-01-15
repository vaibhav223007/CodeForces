number_to_subtract, number_of_subtractions = [int(x) for x in input().split()]

while number_to_subtract > 0 and number_of_subtractions > 0:
    if int(str(number_to_subtract)[-1]) == 0:
        number_to_subtract = int(str(number_to_subtract)[:-1])
        number_of_subtractions -= 1
    else:
        number_to_subtract -= 1
        number_of_subtractions -= 1

print(number_to_subtract)
