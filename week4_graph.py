import random
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

    def perform_edge_contraction(self, a, b):
        """
        Remove edge between a and b, thus all the "a" occurence will be replaced by "b".
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

        # Replace all the existing "a" references by "b"
        for nodes in self.graph.values():
            self.merge_nodes(nodes, a, b)

    def remove_from_node(self, node, value):
        self.graph[node] = [x for x in self.graph[node] if x != value]

    def merge_nodes(self, nodes, a, b):
        for i, value in enumerate(nodes):
            if value == a:
                nodes[i] = b

    def clone(self):
        return Graph(deepcopy(self.graph))

    def sort(self):
        """
        Sort nodes - useful for tests purposes
        """
        for nodes in self.graph.values():
            nodes.sort()

    def perform_random_contraction(self):
        a, b = random.sample(self.graph.keys(), k=2)
        self.perform_edge_contraction(a, b)

    def __len__(self):
        return len(self.graph)


def find_min_cut(graph):
    g = graph.clone()
    while len(g) > 2:
        print('perform contraction')
        g.perform_random_contraction()
    
    key = g.graph.keys()[0]
    return len(g.graph[key])

if __name__ == '__main__':
    graph = load_input_graph('fixtures/karger_min_cut.txt')
    graph.print_stats()

    print(find_min_cut(graph))
