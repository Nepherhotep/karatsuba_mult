from pprint import pprint


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


if __name__ == '__main__':
    graph = load_input_graph('fixtures/karger_min_cut.txt')
    graph.print_stats()
