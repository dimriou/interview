from graph import GRAPH

def bfs(starter):
    visited = [starter]
    queue = [starter]

    while queue:
        current = queue.pop(0)
        for e in GRAPH[current]:
            if e not in visited:
                queue.append(e)
                visited.append(e)

    print(visited)

bfs('A')
