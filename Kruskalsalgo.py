
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    parent[root_a] = root_b


def kruskal(vertices, edges):
    parent = list(range(vertices))
    edges.sort(key=lambda edge: edge[2])

    total_cost = 0
    count = 0

    print("Edges in Minimum Spanning Tree:")

    for u, v, weight in edges:
        a = find(parent, u)
        b = find(parent, v)

        if a != b:
            print(u, "-", v, ":", weight)
            total_cost += weight
            union(parent, a, b)
            count += 1

            if count == vertices - 1:
                break

    if count == vertices - 1:
        print("Total cost =", total_cost)
    else:
        print("MST does not exist; graph is disconnected.")


# Main program
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v weight):")
for i in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

kruskal(n, edges)
1
