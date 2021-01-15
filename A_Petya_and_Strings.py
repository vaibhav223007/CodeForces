string1 = input().lower()
string2 = input().lower()
count = 0
index = 0
while index < len(string1):
    if ord(string1[index]) > ord(string2[index]):
        count += 1
        break
    elif ord(string1[index]) < ord(string2[index]):
        count -= 1
        break
    index += 1

print(count)

