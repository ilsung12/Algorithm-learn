# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

# 1. 시작 노드를 큐에 넣습니다.
# 2. 현재 큐의 노드를 빼서 visited 에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가한다.

# 이 과정을 큐가 빌때까지 반복하면 됩니다!

# 현재 방문한 노드와 인접한 노드는 adjacent_node[current_node] 로 구할 수 있습니다!
# 방문하지 않은 걸 확인 하기 위해서는 visited 를 이용하시면 됩니다!


def bfs_queue(adj_graph, start_node):
    queue = [start_node] # 큐에 시작노드
    visited = []

    while queue: # 큐가 있다면
        current_node = queue.pop(0) # 현재 노드에 첫 값을 넣는다.
        visited.append(current_node) # visited 에 현재 노드를 넣는다
        print('adj_graph[current_node]: ', adj_graph[current_node])
        for adjacent_node in adj_graph[current_node]: 
            if adjacent_node not in visited:
                print('adjacent_node', adjacent_node)
                queue.append(adjacent_node)
                print('queue',queue)
                print('visited',visited)

    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!