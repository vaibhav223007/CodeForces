number_of_stone = int(input())
stones = input()

index = 0
count = 0
while index < len(stones) - 1:
    if stones[index] == stones[index + 1]:
        count += 1
    index += 1

print(count)
