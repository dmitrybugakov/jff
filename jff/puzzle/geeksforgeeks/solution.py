from collections import deque
from queue import Queue
from typing import Dict

from jff.puzzle.geeksforgeeks.graph import GraphDictionary
from jff.puzzle.geeksforgeeks.stack import Stack


def breadth_first_search(graph: GraphDictionary, start: str) -> None:
    if start not in graph.vertices():
        raise ValueError("Graph dosen't contain the vertex : {0}".format(start))

    visited: Dict[str, bool] = dict.fromkeys(graph.vertices(), False)
    visited[start] = True
    queue: deque[str] = Queue(maxsize=100).queue
    queue.append(start)

    while queue:
        start = queue.pop()
        for vertex in graph.full()[start]:
            if not visited[vertex]:
                queue.append(vertex)
                visited[vertex] = True


def depth_first_search(graph: GraphDictionary, start: str) -> None:
    if start not in graph.vertices():
        raise ValueError("Graph dosen't contain the vertex : {0}".format(start))

    visited: Dict[str, bool] = dict.fromkeys(graph.vertices(), False)
    visited[start] = True
    stack: Stack = Stack([start])

    while not stack.is_empty():
        start = stack.pop()
        for vertex in graph.full()[start]:
            if not visited[vertex]:
                stack.push(vertex)
                visited[vertex] = True
