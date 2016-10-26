import networkx as nx

class Graph(object):
    """
    Graph class

    variable nodes holds all the nodes of the graph
    """

    def get_adjacency_matrix(self):
        if hasattr(self, 'adjacency_matrix'):
            return self.adjacency_matrix
        else:
            size = len(self.nodes)
            self.adjacency_matrix = [[0 for x in range(size)] for y in range(size)]
            for node in self.nodes:
                edges = node.edges
                for edge in edges:
                    self.adjacency_matrix[ edge.node1 ][ edge.node2 ] = 1
            return self.adjacency_matrix

    def __init__(self):
        self.nodes = []

class node(object):
    """
    node class

    variable label holds the label of the node
    variable edges holds all the node edges
    """

    # TODO calculate node degree len(edges)

    def __init__(self, label):
        super(node, self).__init__()
        self.label = label
        self.edges = []

class edge(object):
    """
    edge class

    variable node1 holds the index of the first node
    variable node2 holds the index of the second node
    """
    def __init__(self, node1, node2):
        super(edge, self).__init__()
        self.node1 = node1
        self.node2 = node2

def read_file():
    f = nx.read_gml('input/adjnoun.gml')
    g = Graph()
    for nod in nx.nodes(f):
        n = node(nod)
        g.nodes.append(n)
    for nod in g.nodes:
        for edg in nx.edges(f, nod.label):
            e = edge(nx.nodes(f).index(edg[0]), nx.nodes(f).index(edg[1]) )
            nod.edges.append(e)
    return g

def main():
    g = read_file()

if __name__ == "__main__":
    main()
