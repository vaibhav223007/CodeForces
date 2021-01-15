word = input()
lower_count = 0
upper_count = 0

for char in word:
    if char.islower():
        lower_count += 1
    else:
        upper_count += 1

if lower_count > upper_count or lower_count == upper_count:
    print(word.lower())
else:
    print(word.upper())
