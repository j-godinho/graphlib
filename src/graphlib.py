#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx
import random
import networkx as nx
from Queue import Queue



def calc_apl(adj):
    num_nodes = len(adj)
    num_pairs = 0
    total_length = 0
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                num_pairs += 1
                total_length += bfs(adj, i, j)
    return float(total_length) / float(num_pairs)

def bfs(adj, orig, dest):
    size = len(adj)
    queue = Queue()
    visited = [0 for i in range(size)]

    dist = [0 for i in range(size)]

    visited[orig] = 1
    queue.put(orig)

    dist[orig] = 0

    while queue.empty() == False:
        aux = queue.get()

        for u in range(size):
            if adj[aux][u] == 1:
                if visited[u] == 0:
                    dist[u] = dist[aux] + 1
                    queue.put(u)
                    visited[u] = 1
    return dist[dest]

class Graph(object):
    """
    Graph class

    variable nodes holds all the nodes of the graph
    """

    def get_clustering_coefficient(self):
        if hasattr(self, 'clustering_coefficient'):
            return self.clustering_coefficient
        else:
            self.clustering_coefficient = 0
            self.get_adjacency_matrix()
            size = len(self.nodes)
            for index, node in enumerate(self.nodes):
                e = 0
                for edge in node.edges:
                    if edge.source == index:
                        for ind, b in enumerate(self.adjacency_matrix[edge.target]):
                            if b and self.adjacency_matrix[index][ind]:
                                e += 1
                    else:
                        for ind, b in enumerate(self.adjacency_matrix[edge.source]):
                            if b and self.adjacency_matrix[index][ind]:
                                e += 1
                k = node.get_node_degree()
                e /= 2
                if k > 1:
                    div = float((k * (k - 1)) / 2.0)
                    node.clustering_coefficient =  e / div
                else:
                    node.clustering_coefficient = 0
                self.clustering_coefficient += node.clustering_coefficient
            self.clustering_coefficient = self.clustering_coefficient / size
            return self.clustering_coefficient

    def get_adjacency_matrix(self):
        if hasattr(self, 'adjacency_matrix'):
            return self.adjacency_matrix
        else:
            size = len(self.nodes)
            self.adjacency_matrix = [[0 for x in range(size)] for y in range(size)]
            for node in self.nodes:
                edges = node.edges
                for edge in edges:
                    self.adjacency_matrix[ edge.source ][ edge.target ] = 1
            return self.adjacency_matrix

    def __init__(self):
        self.nodes = []

class node(object):
    """
    node class

    variable label holds the label of the node
    variable edges holds all the node edges
    """

    def get_node_degree(self):
        if hasattr(self, 'degree'):
            return self.degree
        else:
            self.degree = len(self.edges)
            return self.degree

    def __init__(self, label):
        super(node, self).__init__()
        self.label = label
        self.edges = []

class edge(object):
    """
    edge class

    variable source holds the index of the source node
    variable target holds the index of the target node
    """
    def __init__(self, source, target):
        super(edge, self).__init__()
        self.source = source
        self.target = target


def read_file(file):
    f = nx.read_gml(file)
    g = Graph()
    for nod in nx.nodes(f):
        n = node(nod)
        g.nodes.append(n)
    for nod in g.nodes:
        for edg in nx.edges(f, nod.label):
            e = edge(nx.nodes(f).index(edg[0]), nx.nodes(f).index(edg[1]) )
            nod.edges.append(e)
    return g


def random_graph(num_nodes, prob):
    adj = [[0 for i in range(num_nodes)] for j in range(num_nodes)]

    for i in range (num_nodes):
        for j in range(num_nodes):
            if(i!=j):
                if(random.random()<prob):
                    adj[i][j] = 1
                    adj[j][i] = 1
    return adj

def main():
    g = read_file('input/clustering.gml')

    #average_path_length = calc_apl(g.get_adjacency_matrix())
    #print('Average path length:', average_path_length)


if __name__ == '__main__':
    main()
