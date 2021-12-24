import math


class Node:
    def __init__(self, key: int, position: tuple = None):
        self.key = key
        self.position = position
        self.in_weight = math.inf
        self.prev_node_key = None
        self.out_going_edges = {}
        self.in_going_edges = {}

    def __repr__(self):
        return f"{self.key}: |edges out| {len(self.out_going_edges)} |edges in| {len(self.in_going_edges)}"
