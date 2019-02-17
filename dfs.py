from graph import GRAPH

def dfs(starter):
    stack = [starter]
    visited = []

    while stack:
        print(stack)
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            for e in GRAPH[current]:
                if e not in stack:
                    stack.append(e)

    print(visited)

dfs('A')
