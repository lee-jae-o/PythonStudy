import heapq

def dijkstra(graph, start):
    # 시작 정점에서 다른 정점까지의 최단 거리를 저장하는 딕셔너리
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # 우선순위 큐를 사용하여 방문할 정점들을 저장
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # 현재 정점을 방문했을 때 더 짧은 경로가 이미 있다면 스킵
        if current_distance > distances[current_vertex]:
            continue

        # 현재 정점과 연결된 정점들을 순회하면서 최단 거리 갱신
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
    # 그래프 정의 (인접 리스트)
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_vertex = 'A'
    shortest_distances = dijkstra(graph, start_vertex)
    print("시작 정점으로부터의 최단 거리:")
    for vertex, distance in shortest_distances.items():
        print(f"{vertex}: {distance}")