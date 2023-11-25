import heapq

def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != '_':
                row, col = divmod(goal_state.index(state[i][j]), 3)
                distance += abs(i - row) + abs(j - col)
    return distance

def generate_moves(state):
    moves = []
    i, j = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == '_')
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= x < 3 and 0 <= y < 3:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
            moves.append((new_state, (x, y)))
    return moves

def a_star(initial_state, goal_state):
    priority_queue = [(manhattan_distance(initial_state, goal_state), initial_state, (0, 0))]
    visited = set()

    while priority_queue:
        _, current_state, (g, _) = heapq.heappop(priority_queue)

        if current_state == goal_state:
            return g

        visited.add(tuple(map(tuple, current_state)))

        for move, position in generate_moves(current_state):
            if tuple(map(tuple, move)) not in visited:
                h = manhattan_distance(move, goal_state)
                heapq.heappush(priority_queue, (g + 1 + h, move, (g + 1, position)))

    return float('inf')

# Example Usage:
initial_state = [[2, 1, 3], [4, 5, 6], [7, 8, '_']]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, '_']]

moves = a_star(initial_state, goal_state)
print(f"Number of moves needed: {moves}")
