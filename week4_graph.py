from pprint import pprint

from copy import deepcopy


def load_input_graph(fixture):
    graph = {}
    with open(fixture) as f:
        for line in f.readlines():
            values = [int(v) for v in line.split()]
            graph[values[0]] = values[1:]
    return Graph(graph)


class Graph:
    def __init__(self, d):
        self.graph = d

    def pprint(self):
        pprint(self.graph)

    def print_stats(self):
        print('Nodes: {}'.format(len(self.graph)))

    def replace_edge(self, a, b):
        """
        We remove edge between a and b. We remove a and move all the existing relations into b.
        :return:
        """
        assert a in self.graph[b], "Can't pop edge - reference found <{}>---<{}>".format(a, b)
        assert b in self.graph[a], "Can't pop edge - reference found <{}>---<{}>".format(b, a)

        # Remove edge <a>---<b>
        self.remove_from_node(a, b)
        self.remove_from_node(b, a)

        # Remove node from graph
        refs = self.graph.pop(a)

        # Add remaining references from a into b
        self.graph[b].extend(refs)
        self.graph[b].extend(refs)

        # Replace all the existing "a" references by "b"
        for nodes in self.graph.values():
            self.merge_nodes(nodes, a, b)

    def remove_from_node(self, node, value):
        self.graph[node] = [x for x in self.graph[node] if x != value]

    def merge_nodes(self, nodes, a, b):
        double_edge = 0
        for i, value in enumerate(nodes):
            if value == a:
                nodes[i] = b
                double_edge += 1

        # double edge
        for i in range(double_edge):
            nodes.append(b)

    def clone(self):
        return Graph(deepcopy(self.graph))

    def sort(self):
        """
        Sort nodes - useful for tests purposes
        """
        for nodes in self.graph.values():
            nodes.sort()


if __name__ == '__main__':
    graph = load_input_graph('fixtures/karger_min_cut.txt')
    graph.print_stats()
