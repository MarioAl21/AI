from collections import deque

def is_goal(state, goal_state):
    return state == goal_state

def generate_moves(state):
    moves = []
    i, j = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == '_')
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= x < 3 and 0 <= y < 3:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
            moves.append(new_state)
    return moves

def bfs(initial_state, goal_state):
    queue = deque([(initial_state, 0)])
    visited = set()

    while queue:
        current_state, depth = queue.popleft()

        if is_goal(current_state, goal_state):
            print(f"Goal state reached! Depth: {depth}")
            return depth

        print(f"Current State (Depth {depth}):")
        for row in current_state:
            print(row)
        print()

        visited.add(tuple(map(tuple, current_state)))

        for move in generate_moves(current_state):
            if tuple(map(tuple, move)) not in visited:
                print(f"Enqueuing new state (Depth {depth + 1}):")
                for row in move:
                    print(row)
                print()
                queue.append((move, depth + 1))

    print("Goal state not reached.")
    return float('inf')

# Example Usage:
initial_state = [[2, 1, 3], [4, 5, 6], [7, 8, '_']]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, '_']]

moves = bfs(initial_state, goal_state)
print(f"Number of moves needed: {moves}")
