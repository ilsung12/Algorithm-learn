# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# 1. 시작 노드를 스택에 넣습니다.
# 2. 현재 스택의 노드를 빼서 visited 에 추가한다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 스택에 추가한다.

# 이 과정을 스택이 빌때까지 반복하면 됩니다!

# 현재 방문한 노드와 인접한 노드는 adjacent_node[current_node] 로 구할 수 있습니다!
# 방문하지 않은 걸 확인 하기 위해서는 visited 를 이용하시면 됩니다!


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []
    while stack: # 스텍이 있으면
        current_node = stack.pop() # 스텍의 맨끝에 있는 노드를 현재 노드에 넣음
        visited.append(current_node) # 현재노드는 방문한 기록이니까 visited 에 넣음
        #print('adjacent_graph[current_node] : ', adjacent_graph[current_node])
        for adjacent_node in adjacent_graph[current_node]: 
            #print('adjacent_node : ', adjacent_node)
            if adjacent_node not in visited:
                stack.append(adjacent_node)
                #print('stack : ', stack)
                #print('visited >>> : ', visited)
    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!