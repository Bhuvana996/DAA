
import itertools

n = 4

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = range(1, n)
min_cost = float('inf')
best_path = []

for path in itertools.permutations(cities):
    total_cost = 0
    k = 0

    for city in path:
        total_cost += cost[k][city]
        k = city

    total_cost += cost[k][0]

    if total_cost < min_cost:
        min_cost = total_cost
        best_path = (0,) + path + (0,)

print("Minimum Cost:", min_cost)
print("Optimal Path:", best_path)
