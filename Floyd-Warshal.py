
INF = 999

n = int(input("Enter number of vertices: "))

print("Enter the cost matrix:")
dist = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j],
                             dist[i][k] + dist[k][j])

print("Shortest distance matrix:")
for row in dist:
    print(*row)
