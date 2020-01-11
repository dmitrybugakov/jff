import copy
import unittest

from jff.puzzle.geeksforgeeks.graph import Graph


class BasicTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        graph_description = {'a': ['d'], 'b': ['c']}
        graph = Graph(graph_description)
        cls.graph = graph

    def test_graph_edges(self) -> None:
        graph: Graph = copy.deepcopy(self.graph)
        result = [{'d', 'a'}, {'c', 'b'}]
        assert graph.edges() == result, "Should be {}".format(result)

    def test_graph_vertices(self) -> None:
        graph: Graph = copy.deepcopy(self.graph)
        result = ['a', 'b']
        assert graph.vertices() == result, "Should be {}".format(result)

    def test_graph_add_vertex(self) -> None:
        graph: Graph = copy.deepcopy(self.graph)
        graph.add_vertex(vertex='f')
        result = ['a', 'b', 'f']
        assert graph.vertices() == result, "Should be {}".format(result)

    def test_graph_add_edge(self) -> None:
        graph: Graph = copy.deepcopy(self.graph)
        graph.add_edge(edge={'a', 'f'})
        result = [{'a', 'd'}, {'b', 'c'}, {'a', 'f'}]
        assert graph.edges() == result, "Should be {}".format(result)


if __name__ == '__main__':
    unittest.main()
