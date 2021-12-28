import copy
from unittest import TestCase

from src.DiGraph import DiGraph


class TestDiGraph(TestCase):

    def test_add_edge(self):
        graph = DiGraph()
        for n in range(4):
            graph.add_node(n)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 0, 1.1)
        graph.add_edge(1, 2, 1.3)
        graph.add_edge(2, 3, 1.1)
        graph.add_edge(1, 3, 1.9)
        self.assertEqual(5, graph.edge_size)
        self.assertEqual(9, graph.get_mc())
        graph.add_edge(3, 2, 10)
        self.assertEqual(6, graph.edge_size)
        self.assertEqual(10, graph.get_mc())

    def test_add_node(self):
        graph = DiGraph()
        for i in range(6):
            graph.add_node(i)
        self.assertEqual(6, graph.node_size)
        self.assertEqual(6, graph.get_mc())
        graph.add_node(57)
        self.assertEqual(7, graph.node_size)
        self.assertEqual(7, graph.get_mc())

    def test_remove_node(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        self.assertEqual(10, graph.node_size)
        self.assertEqual(10, graph.get_mc())
        for i in range(5):
            graph.remove_node(i)
        self.assertEqual(5, graph.node_size)
        self.assertEqual(15, graph.get_mc())

    def test_remove_edge(self):
        graph = DiGraph()
        for n in range(4):
            graph.add_node(n)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 0, 1.1)
        graph.add_edge(1, 2, 1.3)
        graph.add_edge(2, 3, 1.1)
        graph.add_edge(1, 3, 1.9)
        self.assertEqual(5, graph.edge_size)
        self.assertEqual(9, graph.get_mc())
        graph.remove_edge(1, 3)
        self.assertEqual(4, graph.edge_size)
        self.assertEqual(10, graph.get_mc())
        graph.add_edge(1, 3, 2.67)
        graph.remove_edge(1, 3)
        self.assertEqual(4, graph.edge_size)
        self.assertEqual(12, graph.get_mc())

    def test_v_size(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        self.assertEqual(10, graph.node_size)
        for i in range(5):
            graph.remove_node(i)
        self.assertEqual(5, graph.node_size)

    def test_e_size(self):
        graph = DiGraph()
        for n in range(4):
            graph.add_node(n)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 0, 1.1)
        graph.add_edge(1, 2, 1.3)
        graph.add_edge(2, 3, 1.1)
        graph.add_edge(1, 3, 1.9)
        self.assertEqual(5, graph.edge_size)
        self.assertEqual(9, graph.get_mc())
        graph.remove_edge(1, 3)
        self.assertEqual(4, graph.edge_size)
        self.assertEqual(10, graph.get_mc())
        graph.add_edge(1, 3, 2.67)
        graph.remove_edge(1, 3)
        self.assertEqual(4, graph.edge_size)
        self.assertEqual(12, graph.get_mc())

    def test_get_mc(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        self.assertEqual(10, graph.node_size)
        self.assertEqual(10, graph.get_mc())
        for i in range(5):
            graph.remove_node(i)
        self.assertEqual(5, graph.node_size)
        self.assertEqual(15, graph.get_mc())

    def test_get_all_v(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(1, 2, 4)
        all_nodes = graph.get_all_v()
        nodes = {}
        nodes[2] = graph.nodes[2]
        nodes[1] = graph.nodes[1]
        self.assertEqual(nodes, all_nodes)

    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(1, 2, 4)
        edge_in = graph.all_in_edges_of_node(2)
        self.assertEqual({1: 4}, edge_in)
        graph.add_edge(2, 1, 6.97)
        edge_in = graph.all_in_edges_of_node(1)
        self.assertEqual({2: 6.97}, edge_in)
        graph.add_node(3)
        graph.add_edge(3, 2, 3.2323)
        edge_in = graph.all_in_edges_of_node(2)
        self.assertEqual({1: 4, 3: 3.2323}, edge_in)

    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(1, 2, 4)
        edge_out = graph.all_out_edges_of_node(2)
        self.assertEqual({}, edge_out)
        graph.add_edge(2, 1, 6.97)
        edge_out = graph.all_out_edges_of_node(2)
        self.assertEqual({1: 6.97}, edge_out)
        graph.add_node(3)
        graph.add_edge(2, 3, 4.5)
        edge_out = graph.all_out_edges_of_node(2)
        self.assertEqual({1: 6.97, 3: 4.5}, edge_out)
