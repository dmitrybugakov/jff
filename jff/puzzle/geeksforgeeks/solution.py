from collections import deque
from queue import Queue
from typing import Dict

from jff.puzzle.geeksforgeeks.graph import Graph


def breadth_first_search(graph: Graph, start: str) -> None:
    if start not in graph.vertices():
        raise ValueError("Graph dosen't contain the vertex : {0}".format(start))

    visited: Dict[str, bool] = dict.fromkeys(graph.vertices(), False)
    visited[start] = True
    queue: deque[str] = Queue(maxsize=100).queue
    queue.append(start)

    while queue:
        start = queue.pop()
        print(start)

        for vertex in graph.full()[start]:
            if not visited[vertex]:
                queue.append(vertex)
                visited[vertex] = True


def depth_first_search(graph: Graph, start: str) -> None:
    if start not in graph.vertices():
        raise ValueError("Graph dosen't contain the vertex : {0}".format(start))

    visited: Dict[str, bool] = dict.fromkeys(graph.vertices(), False)
    visited[start] = True
