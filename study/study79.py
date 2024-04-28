def has_cycle(graph):
    visited = set()
    stack = set()

    def dfs(node):
        visited.add(node)
        stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in stack:
                return True

        stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False

if __name__ == "__main__":
    # 그래프 정의 (인접 리스트)
    graph_with_cycle = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': ['B'],
        'E': ['C'],
        'F': ['A']
    }

    graph_without_cycle = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': ['E'],
        'E': [],
        'F': []
    }

    print("그래프에 사이클이 있는지 확인:", has_cycle(graph_with_cycle))
    print("그래프에 사이클이 있는지 확인:", has_cycle(graph_without_cycle))