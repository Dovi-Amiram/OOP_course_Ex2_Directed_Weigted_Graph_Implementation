import json
import math
from typing import List

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        self.g = graph

    def get_graph(self) -> GraphInterface:
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name) as file:
                json_graph = json.load(file)
            node_list = json_graph["Nodes"]
            edge_list = json_graph["Edges"]
            for node in node_list:
                pos_string_list = node["pos"].split(",")
                pos_tuple = float(pos_string_list[0]), float(pos_string_list[1]), float(pos_string_list[2])
                self.g.add(node["id"], pos_tuple)
            for edge in edge_list:
                self.g.add_edge(edge["src"], edge["dest"], edge["w"])
            return True
        except OSError:
            return False

    def save_to_json(self, file_name: str) -> bool:
        if self.g is not None:
            node_list = []
            edge_list = []
            for node in self.g.nodes.values():
                node_tuple = node.position
                node_dict = {"pos": f"{node_tuple[0]},{node_tuple[1]},{node_tuple[2]}", "id": node.key}
                node_list.append(node_dict)
            for key, weight in self.g.edges.items():
                edge_dict = {"src": key[0], "w": weight, "dest": key[1]}
                edge_list.append(edge_dict)
            graph_dict = {"Edges": edge_list, "Nodes": node_list}
            with open(file_name, 'w') as file:
                json.dump(graph_dict, file, indent=4)
            return True
        return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        un_checked_node = self.g.nodes
        for item in un_checked_node:
            un_checked_node[item].in_weight = math.inf
        un_checked_node[id1].in_weight = 0
        result = []
        if id1 == id2:
            return 0, result.append(id1)
        while len(un_checked_node) > 0:
            min_weight_node_key = min(un_checked_node.items, key=lambda node_tuple: node_tuple[1].in_weight)[1].key
            un_checked_node.pop(min_weight_node_key)
            current_node = self.g.nodes[min_weight_node_key]
            for dest in self.g.edges_from_node.get(min_weight_node_key):
                next_node = self.g.nodes[dest]
                current_edge_weight = self.g.edges_from_node(min_weight_node_key)[dest]
                if current_node.in_weight + current_edge_weight <  next_node.in_weight:
                    next_node.in_weight = current_node.in_weight + current_edge_weight
                    next_node.prev_node_key = current_node.key
                    if id2 == next_node.key:
                        result.clear()
                        result.append(id2)
                        while current_node.key != id1:
                            result.insert(0,current_node.key)
                            current_node = self.g.nodes[current_node.prev_node_key]
                        result.insert(0,id1)
        distance = self.g.nodes[id2].in_weight
        return distance, result

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass
