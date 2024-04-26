from collections import deque

def bfs_connected_components(graph):
    visited = set()
    components = []

    for vertex in graph:
        if vertex not in visited:
            component = []
            queue = deque([vertex])

            while queue:
                current_vertex = queue.popleft()
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    component.append(current_vertex)
                    queue.extend(graph[current_vertex])
            
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

    connected_components = bfs_connected_components(graph)
    print("연결 요소:", connected_components)