import collections

def bfs(graph, root):
    visited =set()
    queue =collections.deque([root])
    while queue:
        vertex =queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            for i in graph[vertex]:
                if i not in visited:
                    queue.append(i)

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}
bfs(graph,0)