from typing import Dict, List

from jff.puzzle import leetcode
from jff.puzzle.leetcode import solution
from jff.puzzle import hackerrank
from jff.puzzle.hackerrank import solution
from jff.puzzle import geeksforgeeks
from jff.puzzle.geeksforgeeks import solution
from jff.puzzle.geeksforgeeks.graph import Graph


def main() -> None:
    graph_description: Dict[str, List[str]] = {
        'a': ['b'],
        'b': ['a', 'c', 'd'],
        'd': ['b', 'f'],
        'c': ['b'],
        'f': ['d']
    }
    graph: Graph = Graph(graph_description)
    start: str = 'a'
    geeksforgeeks.solution.breadth_first_search(graph=graph, start=start)


if __name__ == "__main__":
    main()
