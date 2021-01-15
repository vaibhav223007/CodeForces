number_of_stops = int(input())
stops = []
capacity = 0
total_count = []

for i in range(number_of_stops):
    enter_exit = [int(i) for i in input().split()]
    stops.append(enter_exit)

for x in stops:
    capacity -= x[0]
    capacity += x[-1]
    total_count.append(capacity)


print(max(total_count))
