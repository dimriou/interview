from graph import GRAPH

def dfs(visited, node):
    print(node)
    visited.append(node)
    for e in GRAPH[node]:
        if e not in visited:
            dfs(visited, e)

visited = []
dfs(visited, 'A')
print(visited)
