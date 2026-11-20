
INF = 999

n = int(input("Enter number of vertices: "))

print("Enter cost matrix:")
cost = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
visited[0] = True

mincost = 0

print("Selected edges:")

for _ in range(n - 1):
    minimum = INF

    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and cost[i][j] < minimum:
                    minimum = cost[i][j]
                    u, v = i, j

    print(u, "-", v, ":", minimum)

    mincost += minimum
    visited[v] = True

print("Minimum cost =", mincost)
