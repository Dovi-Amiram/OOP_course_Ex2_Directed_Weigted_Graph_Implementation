import math


class Node:

    def __init__(self, key: int, position: tuple = None):
        self.key = key
        self.position = position
        self.in_weight = math.inf
        self.prev_node_key = None

    def __int__(self, node):
        self.key = node.key
        self.in_weight = node.in_weight
        self.prev_node_key = node.prev_node_key
        self.position = node.position


