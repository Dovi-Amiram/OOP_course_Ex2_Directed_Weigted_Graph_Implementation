from GraphInterface import GraphInterface
from Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.edges_from_node = {}
        self.edges_to_node = {}
        self.mc = 0
        self.node_size = 0
        self.edge_size = 0

    def __str__(self):
        return "Graph:  |V|={} , |E|={}".format(self.node_size, self.edge_size)

    def v_size(self) -> int:
        return self.node_size

    def e_size(self) -> int:
        return self.edge_size

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes.keys() and id2 in self.nodes.keys() and (id1, id2) not in self.edges.keys():
            self.edges[(id1, id2)] = weight
            self.edges_from_node.get(id1)[id2] = weight
            self.edges_to_node.get(id2)[id1] = weight
            self.edge_size += 1
            self.mc += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.nodes.keys():
            self.nodes[node_id] = Node(node_id, pos)
            self.edges_from_node[node_id] = {}
            self.edges_to_node[node_id] = {}
            self.node_size += 1
            self.mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes.keys():
            self.nodes.pop(node_id)
            for key in self.edges:
                if node_id in key:
                    self.remove_edge(key[0], key[1])
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        key = (node_id1, node_id2)
        if key in self.edges.keys():
            self.edges.pop(key)
            self.edges_from_node[node_id1].pop(node_id2)
            self.edges_to_node[node_id2].pop(node_id1)
            self.edge_size -= 1
            self.mc += 1
            return True
        return False

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        return self.edges_to_node[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        return self.edges_from_node[id1]

