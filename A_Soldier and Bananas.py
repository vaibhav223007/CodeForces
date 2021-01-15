first, money_have, to_buy = [int(x) for x in input().split()]

total_bill = 0

for i in range(1, to_buy+1):
    total_bill += i*first

money_borrowed = total_bill - money_have

if money_borrowed < 0:
    print(0)
else:
    print(money_borrowed)
