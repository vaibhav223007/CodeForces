name = input()

name_length = len(set(name))

if name_length % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

