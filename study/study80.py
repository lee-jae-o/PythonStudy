def dfs_shortest_paths(graph, start):
    paths = {start: [start]}

    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in paths:
                paths[neighbor] = paths[node] + [neighbor]
                dfs(neighbor)

    dfs(start)
    return paths

if __name__ == "__main__":
    # 그래프 정의 (인접 리스트)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_vertex = 'A'
    shortest_paths = dfs_shortest_paths(graph, start_vertex)
    print("시작 정점으로부터의 최단 경로:")
    for vertex, path in shortest_paths.items():
        print(f"{start_vertex} -> {vertex}: {' -> '.join(path)}")
