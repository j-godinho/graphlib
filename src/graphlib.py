import networkx as nx

class node(object):
    """docstring for node."""
    def __init__(self, arg):
        super(node, self).__init__()
        self.arg = arg

def read_file():
    g = nx.read_gml('input/adjnoun.gml')
    nodes = nx.nodes(g)
    size = nx.number_of_nodes(g)
    adj = [[0 for x in range(size)] for y in range(size)]
    for node in nodes:
        edges = nx.edges(g, node)
        for edge in edges:
            adj[ nodes.index(edge[0]) ][ nodes.index(edge[1]) ] = 1
    return adj

def main():
    adj = read_file()

if __name__ == "__main__":
    main()
