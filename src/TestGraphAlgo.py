import math
from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        a_g = GraphAlgo()
        self.assertIsNotNone(a_g)
        g = DiGraph()
        g.add_node(1)
        a_g = GraphAlgo(g)
        self.assertIsNotNone(a_g)
        self.assertEqual(a_g.get_graph(), g)

    def test_load_save_from_json(self):
        a_g = GraphAlgo()
        a_g.load_from_json("..\data\A0.json")
        self.assertEqual(11, a_g.get_graph().v_size())
        self.assertEqual(22, a_g.get_graph().e_size())
        a_g.save_to_json("test_save.json")
        a2_g = GraphAlgo()
        a2_g.load_from_json("test_save.json")
        self.assertEqual(a_g.get_graph().e_size(), a2_g.get_graph().e_size())
        self.assertEqual(a_g.get_graph().v_size(), a2_g.get_graph().v_size())

    def test_shortest_path(self):
        g = DiGraph()
        for i in range(1, 5):
            g.add_node(i)
        g.add_edge(2, 1, 1)
        g.add_edge(2, 3, 0.3)
        g.add_edge(3, 1, 0.3)
        g.add_edge(3, 4, 0.1)
        g.add_edge(4, 1, 0.1)
        a_g = GraphAlgo(g)
        path = a_g.shortest_path(2, 1)
        self.assertEqual((0.5, [2, 3, 4, 1]), path)
        a_g.get_graph().remove_node(4)
        path = a_g.shortest_path(2, 1)
        self.assertEqual((0.6, [2, 3, 1]), path)

    def test_tsp(self):
        g = DiGraph()
        for i in range(6):
            g.add_node(i)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 2, 3)
        g.add_edge(1, 3, 1)
        g.add_edge(3, 2, 0.5)
        g.add_edge(3, 5, 0.1)
        g.add_edge(5, 2, 0.1)
        a_g = GraphAlgo(g)
        cities = ([0, 1, 3, 5, 2], 2.2)
        self.assertEqual(cities, a_g.TSP([0, 2, 3]))
        a_g.get_graph().remove_node(5)
        cities = ([0, 1, 3, 2], 2.5)
        self.assertEqual(cities, a_g.TSP([0, 2, 3]))
        self.assertEqual(([0], 0), a_g.TSP([0]))
        self.assertEqual(([], math.inf), a_g.TSP([2, 4]))

    def test_center_point(self):
        a_g = GraphAlgo()
        a_g.load_from_json("..\data\A0.json")
        self.assertEqual((7, 6.806805834715163), a_g.centerPoint())
        a_g.load_from_json("..\data\A1.json")
        self.assertEqual((8, 9.925289024973141), a_g.centerPoint())
        a_g.load_from_json("..\data\A2.json")
        self.assertEqual((0, 7.819910602212574), a_g.centerPoint())
        a_g.load_from_json("..\data\A3.json")
        self.assertEqual((2, 8.182236568942237), a_g.centerPoint())
        a_g.load_from_json("..\data\A4.json")
        self.assertEqual((6, 8.071366078651435), a_g.centerPoint())
        a_g.load_from_json("..\data\A5.json")
        self.assertEqual((40, 9.291743173960954), a_g.centerPoint())
