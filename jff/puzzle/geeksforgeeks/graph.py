from typing import List, Dict, Set, Any


class Graph:
    pass


class GraphMatrix(Graph):

    def __init__(self: Any, size: int = None, matrix: List[List[int]] = None):
        """ initializes a graph object """
        if size or matrix:
            if size:
                self.__init_with_size_matrix__(size)
            if matrix:
                self.__init_with_matrix__(matrix)
        else:
            self.__init_default__()

    def full(self: Any) -> List[List[int]]:
        """ returns the graph dictionary"""
        return self.__graph_matrix__

    def add_edge(self: Any, v1: int, v2: int, weight: int) -> None:
        """ add edge in graph """
        if v1 in self.vertices() and v2 in self.vertices():
            self.__graph_matrix__[v1][v2] = weight
        else:
            raise Exception("Matrix dosen't contain vertices {0} and {1}".format(v1, v2))

    def add_vertex(self):
        """ add vertex in graph """
        self.__size__ += 1
        for vertices in self.__graph_matrix__:
            vertices.append(0)
        self.__graph_matrix__.append([0] * self.__size__)

    def vertices(self: Any) -> List[int]:
        """ returns the vertices of a graph """
        return list([row for row in range(self.__size__)])

    def show(self: Any) -> None:
        """ prints the graph """
        print(self.__graph_matrix__)

    def __init_with_matrix__(self: Any, graph_matrix: List[List[int]]) -> None:
        """ initializes a graph object """
        self.__size__ = len(graph_matrix)
        self.__graph_matrix__ = graph_matrix

    def __init_with_size_matrix__(self: Any, size: int) -> None:
        """ initializes a graph object """
        self.__size__ = size
        self.__graph_matrix__ = [[0] * size for _ in range(size)]

    def __init_default__(self: Any) -> None:
        """ initializes a graph object """
        self.__size__ = 0
        self.__graph_matrix__ = []


class GraphDictionary(Graph):

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

    def show(self: Any) -> None:
        """ prints the graph """
        print(self.__graph_dict__)

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
