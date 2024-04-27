def dfs_connected_components(graph):
    visited = set()
    components = []

    def dfs(vertex, component):
        visited.add(vertex)
        component.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for vertex in graph:
        if vertex not in visited:
            component = []
            dfs(vertex, component)
            components.append(component)

    return components

if __name__ == "__main__":
    # 그래프 정의 (인접 리스트)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'],
        'G': ['H'],
        'H': ['G']
    }

    connected_components = dfs_connected_components(graph)
    print("연결 요소:", connected_components)