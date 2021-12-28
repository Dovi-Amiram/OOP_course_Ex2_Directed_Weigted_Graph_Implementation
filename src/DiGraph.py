from GraphInterface import GraphInterface
from Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.mc = 0
        self.node_size = 0
        self.edge_size = 0

    def __repr__(self):
        return f"Graph: |V| = {self.node_size} , |E| = {self.edge_size}"

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.node_size

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.edge_size

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 in self.nodes.keys() and id2 in self.nodes.keys() and (id1, id2) not in self.edges.keys():
            self.edges[(id1, id2)] = weight
            self.nodes[id1].out_going_edges[id2] = weight
            self.nodes[id2].in_going_edges[id1] = weight
            self.edge_size += 1
            self.mc += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if node_id not in self.nodes.keys():
            self.nodes[node_id] = Node(node_id, pos)
            self.node_size += 1
            self.mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        if node_id in self.nodes.keys():
            self.nodes.pop(node_id)
            self.node_size -= 1
            self.mc += 1
            for key in self.edges:
                if node_id in key:
                    self.remove_edge(key[0], key[1])
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        key = (node_id1, node_id2)
        if key in self.edges.keys():
            self.edges.pop(key)
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
        return self.nodes[id1].in_going_edges

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        return self.nodes[id1].out_going_edges

    def reset_all_visited(self):
        for key in self.nodes:
            self.nodes[key].visited = False
