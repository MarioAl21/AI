from collections import deque
import time

class PuzzleNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

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

def expand_node(node):
    expanded_nodes = []
    actions = [move_up, move_down, move_left, move_right]
    for action in actions:
        child_state = action(node.state)
        if child_state is not None:
            child_node = PuzzleNode(child_state, parent=node, action=action.__name__)
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

def bfs(initial_state):
    initial_node = PuzzleNode(initial_state)
    frontier = deque([(initial_node, 1)])
    explored = set()
    numberChild = 1;

    while frontier:
        current_node, depth = frontier.popleft()
        parent = f"Root (Depth: {depth})";
        
        if current_node.state != initial_state:
         parent = f"Parent (Depth: {depth})";
        
        print(f"{parent}: \n {current_node.state[0:3]}\n {current_node.state[3:6]}\n {current_node.state[6:9]}");

        if is_goal_state(current_node.state):
            return reconstruct_path(current_node)

        explored.add(current_node.state)

        for child_node in expand_node(current_node):
            if child_node.state not in explored and child_node not in frontier: 
                print("Child ", numberChild, f": \n {child_node.state[0:3]}\n {child_node.state[3:6]}\n {child_node.state[6:9]}");
                numberChild += 1;
                frontier.append((child_node, depth + 1))
        numberChild = 1;
        print();

    return None

if __name__ == "__main__":
    start_time = time.time()
    initial_state = ('_',  2, 3, 
                     4, 1, 6,
                     7, 5, 8)
    solution_path = bfs(initial_state)
    end_time = time.time()

    print("\n\n\n******************");

    if solution_path:
        print("Solution found!")
        for step, (state, action) in enumerate(solution_path):
            print(f"Step {step + 1}: Move {action}\n{state[0:3]}\n{state[3:6]}\n{state[6:9]}\n")
    else:
        print("No solution found.")

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
