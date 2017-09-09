from unittest import TestCase

from week4_graph import Graph


class TestGraph(TestCase):
    def test_replace_edge(self):
        """
        We use graph below

        <1> --- <2>
         |       |
        <4> --- <3>


        We want to replace 2 with 3:

           <1>
          /    \
        <4> -- <3>

        """
        g = Graph({1: [2, 4],
                   2: [1, 3],
                   3: [2, 4],
                   4: [1, 3]})

        g.replace_edge(2, 3)
        g.sort()

        expected = {1: [3, 4],
                    3: [1, 4],
                    4: [1, 3]}

        self.assertEqual(g.graph, expected)


    def replace_multiple_nodes(self):
        """
        We use graph below

            ---
        <1> --- <2>
         |      |||
        <4> --- <3>

        We want to replace 2 with 3:

        <1> --[5 times]
         |        |
        <4> ---- <3>
        """
        g = Graph({1: [2, 4],
                   2: [1, 3],
                   3: [2, 4],
                   4: [1, 3]})

        g.replace_edge(2, 3)
        g.sort()

        expected = {1: [3, 3, 4],
                    3: [1, 1, 4],
                    4: [1, 3]}

        self.assertEqual(g.graph, expected)
