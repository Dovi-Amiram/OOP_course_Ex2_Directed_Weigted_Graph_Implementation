import json
import math
import copy
from typing import List
from GraphAlgoInterface import GraphAlgoInterface
from  GraphInterface import GraphInterface
from  DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        self.g = graph

    """This abstract class represents an interface of a graph."""

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        try:
            with open(file_name) as file:
                json_graph = json.load(file)
            node_list = json_graph["Nodes"]
            edge_list = json_graph["Edges"]
            for node in node_list:
                pos_string_list = node["pos"].split(",")
                pos_tuple = float(pos_string_list[0]), float(pos_string_list[1]), float(pos_string_list[2])
                self.g.add_node(node["id"], pos_tuple)
            for edge in edge_list:
                self.g.add_edge(edge["src"], edge["dest"], edge["w"])
            return True
        except OSError:
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        if self.g is not None:
            node_list = []
            edge_list = []
            for node in self.g.nodes.values():
                pos_tuple = node.position
                node_dict = {"pos": f"{pos_tuple[0]},{pos_tuple[1]},{pos_tuple[2]}", "id": node.key}
                node_list.append(node_dict)
            for key, weight in self.g.edges.items():
                edge_dict = {"src": key[0], "w": weight, "dest": key[1]}
                edge_list.append(edge_dict)
            graph_dict = {"Edges": edge_list, "Nodes": node_list}
            with open(file_name, "w") as file:
                json.dump(graph_dict, file, indent=4)
            return True
        return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        unchecked_nodes = copy.copy(self.g.nodes)
        for item in unchecked_nodes:
            unchecked_nodes[item].in_weight = math.inf
        unchecked_nodes[id1].in_weight = 0
        result = []
        if id1 == id2:
            return 0, result.append(id1)
        while len(unchecked_nodes) > 0:
            min_weight_node_key = min(unchecked_nodes.items(), key=lambda node_tuple: node_tuple[1].in_weight)[1].key
            current_node = unchecked_nodes.pop(min_weight_node_key)
            for neighbour in self.g.edges_from_node.get(min_weight_node_key):
                next_node = self.g.nodes.get(neighbour)
                current_edge_weight = self.g.edges_from_node.get(min_weight_node_key)[neighbour]
                if current_node.in_weight + current_edge_weight < next_node.in_weight:
                    next_node.in_weight = current_node.in_weight + current_edge_weight
                    next_node.prev_node_key = current_node.key
                    if next_node.key == id2:
                        result.clear()
                        result.append(id2)
                        while current_node.key != id1:
                            result.insert(0, current_node.key)
                            current_node = self.g.nodes[current_node.prev_node_key]
                        result.insert(0, id1)
        distance = self.g.nodes[id2].in_weight
        return distance, result


    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError
