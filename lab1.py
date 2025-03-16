def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth):
        path = dls(graph, start, goal, depth)
        if path:
            return path
    return []
def dls(graph, start, goal, depth):
    if start == goal:
        return [start]
    if depth == 0:
        return []
    for neighbor in graph[start]:
        path = dls(graph, neighbor, goal, depth - 1)
        print(path)
        if path:
            return [start] + path
    return []
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
start_vertex = 'A'
goal_vertex = 'F'
max_depth = 5
path = iddfs(graph, start_vertex, goal_vertex, max_depth)
print(path)

