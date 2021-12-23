import math


class Node:
    def __init__(self, key: int, position: tuple = None):
        self.key = key
        self.position = position
        self.in_weight = math.inf
        self.prev_node_key = None
