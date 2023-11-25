from pprint import pprint
from collections import deque

class PuzzleNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

node = PuzzleNode((1, 2, 4));

def bfs(state):
 f = deque([state]);
 