def bellman_ford(graph, start):
    # 그래프의 정점 수
    num_vertices = len(graph)
    
    # 시작 정점으로부터의 최단 거리를 저장하는 딕셔너리 초기화
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # 간선 수
    num_edges = sum(len(adj) for adj in graph.values())

    # 최단 거리 갱신
    for _ in range(num_vertices - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    # 음수 사이클 확인
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                print("음수 사이클이 존재합니다.")
                return

    return distances

if __name__ == "__main__":
    # 그래프 정의 (인접 리스트)
    graph = {
        'A': {'B': -1, 'C': 4},
        'B': {'C': 3, 'D': 2, 'E': 2},
        'C': {},
        'D': {'B': 1, 'C': 5},
        'E': {'D': -3}
    }

    start_vertex = 'A'
    shortest_distances = bellman_ford(graph, start_vertex)
    print("시작 정점으로부터의 최단 거리:")
    for vertex, distance in shortest_distances.items():
        print(f"{vertex}: {distance}")