number_of_questions = int(input())
number_of_friend = 3
opinion_list = []
count = 0

for question in range(number_of_questions):
    opinion_list = [int(x) for x in input().split()]
    if opinion_list.count(1) >= 2:
        count += 1

print(count)

