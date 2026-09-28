import collections

def dfs(graph,root):
    visited=set()
    stack =[root]
    while stack:
        vertex =stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            for i in graph[vertex]:
                if i not in visited:
                    stack.append(i)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}
dfs(graph,0)
