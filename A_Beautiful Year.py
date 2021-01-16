input_year = int(input())

while True:
    lst = []

    for digit in str(input_year+1):
        lst.append(digit)

    if len(set(lst)) == len(lst):
        print("".join(lst))
        break
    else:
        input_year += 1
