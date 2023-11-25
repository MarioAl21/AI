from collections import deque
import time

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g  # cost to reach this state
        self.h = h  # heuristic estimate

def get_blank_index(state):
    return state.index('_')

def move_up(state):
    blank_index = get_blank_index(state)
    if blank_index >= 3:
        new_state = list(state)
        new_state[blank_index], new_state[blank_index - 3] = new_state[blank_index - 3], new_state[blank_index]
        return tuple(new_state)
    return None

def move_down(state):
    blank_index = get_blank_index(state)
    if blank_index < 6:
        new_state = list(state)
        new_state[blank_index], new_state[blank_index + 3] = new_state[blank_index + 3], new_state[blank_index]
        return tuple(new_state)
    return None

def move_left(state):
    blank_index = get_blank_index(state)
    if blank_index % 3 != 0:
        new_state = list(state)
        new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]
        return tuple(new_state)
    return None

def move_right(state):
    blank_index = get_blank_index(state)
    if (blank_index + 1) % 3 != 0:
        new_state = list(state)
        new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]
        return tuple(new_state)
    return None

def manhattan_distance(state):
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, '_')
    distance = 0
    for i in range(1, 9):
        current_index = state.index(i)
        goal_index = goal_state.index(i)
        distance += abs(current_index // 3 - goal_index // 3) + abs(current_index % 3 - goal_index % 3)
    return distance

def expand_node(node):
    expanded_nodes = []
    actions = [move_up, move_down, move_left, move_right]
    for action in actions:
        child_state = action(node.state)
        if child_state is not None:
            g_cost = node.g + 1  # cost to reach the child state
            h_cost = manhattan_distance(child_state)  # heuristic estimate
            child_node = PuzzleNode(child_state, parent=node, action=action.__name__, g=g_cost, h=h_cost)
            expanded_nodes.append(child_node)
    return expanded_nodes

def is_goal_state(state):
    return state == (1, 2, 3, 
		     4, 5, 6, 
                     7, 8, '_')

def reconstruct_path(node):
    path = []
    while node is not None:
        path.append((node.state, node.action))
        node = node.parent
    return path[::-1]

def a_star(initial_state):
    initial_node = PuzzleNode(initial_state, g=0, h=manhattan_distance(initial_state))
    frontier = [initial_node]
    explored = set()

    while frontier:
        frontier.sort(key=lambda node: node.g + node.h)  # Sort by f(n) = g(n) + h(n)
        current_node = frontier.pop(0)

        if is_goal_state(current_node.state):
            return reconstruct_path(current_node)

        explored.add(current_node.state)

        for child_node in expand_node(current_node):
            if child_node.state not in explored and child_node not in frontier:
                frontier.append(child_node)

    return None

if __name__ == "__main__":
    initial_state = (1,  2, 3, 
                     4, 6, '_',
                     7, 5, 8)
    
    start_time = time.time()
    solution_path = a_star(initial_state)
    end_time = time.time()

    if solution_path:
        print("Solution found!")
        for step, (state, action) in enumerate(solution_path):
            print(f"Step {step + 1}: Move {action}\n{state[0:3]}\n{state[3:6]}\n{state[6:9]}\n")
    else:
        print("No solution found.")

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")

