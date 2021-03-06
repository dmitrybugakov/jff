import copy
import unittest
from typing import Any, Set

from jff.puzzle.geeksforgeeks.graph import GraphDictionary


class BasicTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls: Any) -> None:
        graph_description = {'a': ['d'], 'b': ['c']}
        graph = GraphDictionary(graph_description)
        cls.graph = graph
        cls.errorMessage = "Should be {0}"

    def test_graph_dictionary_edges(self: Any) -> None:
        graph: GraphDictionary = copy.deepcopy(self.graph)
        result = [{'d', 'a'}, {'c', 'b'}]
        assert graph.edges() == result, self.errorMessage.format(result)

    def test_graph_dictionary_vertices(self: Any) -> None:
        graph: GraphDictionary = copy.deepcopy(self.graph)
        result = ['a', 'b']
        assert graph.vertices() == result, self.errorMessage.format(result)

    def test_graph_dictionary_add_vertex(self: Any) -> None:
        graph: GraphDictionary = copy.deepcopy(self.graph)
        graph.add_vertex(vertex='f')
        result = ['a', 'b', 'f']
        assert graph.vertices() == result, self.errorMessage.format(result)

    def test_graph_dictionary_add_edge(self: Any) -> None:
        graph: GraphDictionary = copy.deepcopy(self.graph)
        edge: Set[str] = {'a', 'f'}
        graph.add_edge(edge=edge)
        result = [{'a', 'd'}, {'b', 'c'}, {'a', 'f'}]
        assert graph.edges() == result, self.errorMessage.format(result)


if __name__ == '__main__':
    unittest.main()
