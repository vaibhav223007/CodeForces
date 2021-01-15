number_input = input()

splitted_numbers = number_input.split("+")
int_splitted_number = list(map(int, splitted_numbers))
int_splitted_number.sort()

original_number = "+".join(str(ele) for ele in int_splitted_number)
print(original_number)

