from typing import List, Dict, Set, Any


class Graph:

    def __init__(self: Any, graph_dict: Dict[str, List[str]] = None) -> None:
        """ initializes a graph object """
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict__ = graph_dict

    def full(self: Any) -> Dict[str, List[str]]:
        """ returns the graph dictionary"""
        return self.__graph_dict__

    def vertices(self: Any) -> List[str]:
        """ returns the vertices of a graph """
        return list(self.__graph_dict__.keys())

    def edges(self: Any) -> List[Set[str]]:
        """ returns the edges of a graph """
        return self.__generate_edges__()

    def add_vertex(self: Any, vertex: str) -> None:
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done. """
        if vertex not in self.__graph_dict__:
            self.__graph_dict__[vertex] = []

    def add_edge(self: Any, edge: Set[str]) -> None:
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges! """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict__:
            self.__graph_dict__[vertex1].append(vertex2)
        else:
            self.__graph_dict__[vertex1] = [vertex2]

    def __generate_edges__(self: Any) -> List[Set[str]]:
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices """
        edges: List[Set[str]] = []
        for vertex in self.__graph_dict__:
            for neighbour in self.__graph_dict__[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self: Any) -> str:
        res = "vertices: "
        for k in self.__graph_dict__:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges__():
            res += str(edge) + " "
        return res
