# Kruskal.py

parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]

def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1

        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(graph):
    for v in graph['vertices']:
        make_set(v)

    mst = []
    cost = 0

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, v, u = edge

        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
            cost += edge[0]

    return (mst, cost)

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (15, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F'),
    ]
}

route, cost = kruskal(graph)

print('> Graph Vertices <')
print(graph['vertices'], "\n")

print('> Graph Edges < ')
for edge in graph['edges']:
    print(edge)
print()
'''
> Graph Vertices <
['A', 'B', 'C', 'D', 'E', 'F', 'G']

> Graph Edges <
(5, 'A', 'D')
(5, 'C', 'E')
(5, 'D', 'A')
(5, 'E', 'C')
(6, 'D', 'F')
(6, 'F', 'D')
(7, 'A', 'B')
(7, 'B', 'A')
(7, 'B', 'E')
(7, 'D', 'E')
(7, 'E', 'B')
(8, 'B', 'C')
(8, 'C', 'B')
(8, 'E', 'F')
(8, 'F', 'E')
(9, 'B', 'D')
(9, 'D', 'B')
(9, 'E', 'G')
(9, 'G', 'E')
(11, 'F', 'G')
(11, 'G', 'F')
(15, 'E', 'D')
'''

print('- Kruskal Minimum Spanning Tree Algorithm -')
print('>   Route  <')
for edge in route:
    print(edge)
print('Cost : %6d' % cost)
'''
- Kruskal Minimum Spanning Tree Algorithm -
>   Route  <
(5, 'A', 'D')
(5, 'C', 'E')
(6, 'D', 'F')
(7, 'A', 'B')
(7, 'B', 'E')
(9, 'E', 'G')
Cost :     39
'''
