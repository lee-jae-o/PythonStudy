from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    
    while queue:
        current_node, path = queue.popleft()
        if current_node == end:
            return path
        for neighbor in graph[current_node]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

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
    end_vertex = 'F'
    shortest_path = bfs_shortest_path(graph, start_vertex, end_vertex)
    print("최단 경로:", shortest_path)