from typing import List

from jff.puzzle import leetcode
from jff.puzzle.geeksforgeeks.stack import Stack
from jff.puzzle.leetcode import solution
from jff.puzzle import hackerrank
from jff.puzzle.hackerrank import solution
from jff.puzzle import geeksforgeeks
from jff.puzzle.geeksforgeeks import solution
from jff.puzzle.geeksforgeeks.graph import Graph, GraphMatrix


def main() -> None:
    matrix: List[List[int]] = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                               [4, 0, 8, 0, 0, 0, 0, 11, 0],
                               [0, 8, 0, 7, 0, 4, 0, 0, 2],
                               [0, 0, 7, 0, 9, 14, 0, 0, 0],
                               [0, 0, 0, 9, 0, 10, 0, 0, 0],
                               [0, 0, 4, 14, 10, 0, 2, 0, 0],
                               [0, 0, 0, 0, 0, 2, 0, 1, 6],
                               [8, 11, 0, 0, 0, 0, 1, 0, 7],
                               [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    graph: GraphMatrix = GraphMatrix(matrix=matrix)
    graph.show()

if __name__ == "__main__":
    main()
