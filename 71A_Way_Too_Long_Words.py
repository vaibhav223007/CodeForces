# My solution

how_many_input = int(input())
for num in range(how_many_input):
    word = input()
    if len(word) > 10:
        abbreviation = word[0] + str(len(word) - 2) + word[-1]
        print(abbreviation)
    else:
        print(word)

