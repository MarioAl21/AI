class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

def find_goal(state):
    goal = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]

    if state == goal:
        return True
    return False

def get_possible_moves(state):
    possible_moves = []

    # Find the empty space
    empty_row, empty_col = find_empty(state)

    # Check the possible moves
    if empty_row > 0:
        # Move the tile above
        new_state = copy.deepcopy(state)
        new_state[empty_row][empty_col] = new_state[empty_row - 1][empty_col]
        new_state[empty_row - 1][empty_col] = 0
        possible_moves.append(Node(new_state, Node(state, None, None), 'UP'))

    if empty_row < 2:
        # Move the tile below
        new_state = copy.deepcopy(state)
        new_state[empty_row][empty_col] = new_state[empty_row + 1][empty_col]
        new_state[empty_row + 1][empty_col] = 0
        possible_moves.append(Node(new_state, Node(state, None, None), 'DOWN'))

    if empty_col > 0:
        # Move the tile to the left
        new_state = copy.deepcopy(state)
        new_state[empty_row][empty_col] = new_state[empty_row][empty_col - 1]
        new_state[empty_row][empty_col - 1] = 0
        possible_moves.append(Node(new_state, Node(state, None, None), 'LEFT'))

    if empty_col < 2:
        # Move the tile to the right
        new_state = copy.deepcopy(state)
        new_state[empty_row][empty_col] = new_state[empty_row][empty_col + 1]
        new_state[empty_row][empty_col + 1] = 0
        possible_moves.append(Node(new_state, Node(state, None, None), 'RIGHT'))

    return possible_moves

def bfs(start_state):
    frontier = []
    explored = set()

    # Add the start state to the frontier
    frontier.append(Node(start_state, None, None))

    while frontier:
        # Choose the next node to explore
        current_node = frontier.pop(0)

        # Check if we've reached the goal
        if find_goal(current_node.state):
            return current_node

        # Add the current state to explored
        explored.add(tuple(current_node.state))

        # Explore the possible moves
        possible_moves = get_possible_moves(current_node.state)

        for move in possible_moves:
            # Check if the move has already been explored
            if tuple(move.state) in explored:
                continue

            # Add the move to the frontier
            frontier.append(move)

    return None

def solve_8_puzzle(start_state):
    solution = bfs(start_state)

    if solution is None:
        print('No solution found')
        return

    # Print the solution
    path = []
    while solution:
        path.append(solution.action)
        solution = solution.parent

    path.reverse()
    print('Solution:', path)

# Example usage
start_state = [[2, 8, 3],
               [1, 0, 4],
               [7, 6, 5]]
solve_8_puzzle(start_state)
