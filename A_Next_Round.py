n, k = [int(x) for x in input().split()]

# scores = [int(input()) for i in range(n)]
scores = [int(y) for y in input().split()]

count = 0

for ele in scores:
    if ele >= scores[k - 1] and ele > 0:
        count += 1

print(count)

