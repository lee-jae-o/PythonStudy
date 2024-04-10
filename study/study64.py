def floyd_warshall(graph):
    # 그래프의 크기
    n = len(graph)
    
    # 최단 거리를 저장하는 행렬 초기화
    dist = [[float('inf')] * n for _ in range(n)]

    # 자기 자신으로의 거리는 0으로 초기화
    for i in range(n):
        dist[i][i] = 0

    # 그래프의 간선 정보를 행렬에 반영
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    # 최단 거리 행렬 계산
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

if __name__ == "__main__":
    # 그래프 정의 (인접 행렬)
    graph = [
        [0, 3, 0, 7],
        [8, 0, 2, 0],
        [5, 0, 0, 1],
        [2, 0, 0, 0]
    ]

    shortest_distances = floyd_warshall(graph)
    print("최단 거리 행렬:")
    for row in shortest_distances:
        print(row)