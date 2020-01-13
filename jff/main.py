from jff.puzzle import leetcode
from jff.puzzle.geeksforgeeks.stack import Stack
from jff.puzzle.leetcode import solution
from jff.puzzle import hackerrank
from jff.puzzle.hackerrank import solution
from jff.puzzle import geeksforgeeks
from jff.puzzle.geeksforgeeks import solution
from jff.puzzle.geeksforgeeks.graph import Graph


def main() -> None:
    graph_description = {
        'a': ['b'],
        'b': ['a', 'c', 'd'],
        'd': ['b'],
        'c': ['b']
    }
    graph: Graph = Graph(graph_description)
    start: str = 'a'
    geeksforgeeks.solution.depth_first_search(graph=graph, start=start)


if __name__ == "__main__":
    main()
