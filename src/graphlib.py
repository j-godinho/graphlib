#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import random
from Queue import Queue

class graph(object):
    """
    graph class

    Atributes:
        nodes (array:node): List of all the nodes of the graph.

    Methods:
        get_adjacency_matrix(array:(array:int)): Returns the adjacency matrix of the graph.
        get_average_path_length(float): Returns the average path length of the graph.
        get_clustering_coefficient(float): Returns the clustering coefficient of the graph.
    """

    # TODO change the len(self.nodes) to a atribute

    def get_nodes(self):
        return self.nodes

    def get_degree_distribution(self):
        if hasattr(self, 'degree_distribution'):
            return self.degree_distribution
        else:
            n = len(self.get_node_degree_histogram())
            num_nodes = len(self.nodes)
            self.degree_distribution = [float(self.degree_histogram[i])/num_nodes for i in range(n)]
            return self.degree_distribution

    def get_cumulative_degree_distribution(self):
        if hasattr(self, 'cumulative_degree_distribution'):
            return self.cumulative_degree_distribution
        else:
            n = len(self.get_degree_distribution())
            self.cumulative_degree_distribution = [0 for j in range(n)]
            for i in range(n):
                for j in range(i, n):
                    self.cumulative_degree_distribution[i] += self.degree_distribution[j]
            return self.cumulative_degree_distribution

    def get_node_degree_histogram(self):
        if hasattr(self, 'degree_histogram'):
            return self.degree_histogram
        else:
            self.get_max_node_degree()
            self.degree_histogram = [0 for j in range(self.max_node_degree + 1)]
            n = len(self.nodes)
            for i in range(n):
                self.degree_histogram[self.nodes[i].degree] += 1
            return self.degree_histogram

    def get_max_node_degree(self):
        if hasattr(self, 'max_node_degree'):
            return self.max_node_degree
        else:
            self.calc_node_degrees()
            self.max_node_degree = 0
            for node in self.nodes:
                if node.degree > self.max_node_degree:
                    self.max_node_degree = node.degree
            return self.max_node_degree

    def calc_node_degrees(self):
        for node in self.nodes:
            node.get_node_degree()

    def get_average_path_length(self):
        if hasattr(self, 'average_path_length'):
            return self.average_path_length
        else:
            num_nodes = len(self.nodes)
            num_pairs = 0
            total_length = 0
            adj = self.get_adjacency_matrix()
            for i in range(num_nodes):
                for j in range(i, num_nodes):
                    if i != j:
                        num_pairs += 1
                        total_length += bfs(adj, i, j)
            self.average_path_length = float(total_length) / float(num_pairs)
            return self.average_path_length

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

    def get_edges(self):
        return self.edges

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

    def get_source(self):
        return self.source

    def get_target(self):
        return self.target

    def __init__(self, source, target):
        super(edge, self).__init__()
        self.source = source
        self.target = target

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

def read_file(file):
    f = nx.read_gml(file)
    g = graph()
    for nod in nx.nodes(f):
        n = node(nod)
        g.nodes.append(n)
    for nod in g.nodes:
        for edg in nx.edges(f, nod.label):
            e = edge(nx.nodes(f).index(edg[0]), nx.nodes(f).index(edg[1]) )
            nod.edges.append(e)
    return g

def generate_random_graph(num_nodes, prob):
    adj = [[0 for i in range(num_nodes)] for j in range(num_nodes)]
    g = graph()
    for i in range(num_nodes):
        label = "node {}".format(i)
        g.nodes.append( node(label) )
    for i in range (num_nodes):
        for j in range(num_nodes):
            if(i!=j):
                if(random.random()<prob):
                    g.nodes[i].edges.append( edge(i, j) )
                    g.nodes[j].edges.append( edge(i, j) )
                    adj[i][j] = 1
                    adj[j][i] = 1
    g.adjacency_matrix = adj
    return g

def generate_barabasi_albert_graph(m0, links, num_nodes):
    adj = [[0 for i in range(num_nodes+m0)] for j in range(num_nodes+m0)]
    g = graph()

    for i in range(num_nodes+m0):
        label = "node {}".format(i)
        g.nodes.append( node(label) )

    for i in range(m0):
        index = random.randint(0, m0-1)
        while (index == i and adj[i][index]==1):
            index = random.randint(0, m0-1)
        g.nodes[i].edges.append( edge(i, index))
        g.nodes[index].edges.append( edge(i, index))
        adj[i][index] = 1
        adj[index][i] = 1

    nodes_added = 0
    for i in range(num_nodes):
        rand_nums = []
        for k in range (links):
            value = random.randint(0, m0+nodes_added-1)
            while(value in rand_nums):
                value = random.randint(0, m0 + nodes_added-1)
            g.nodes[m0+i].edges.append(edge(m0+i, value))
            g.nodes[value].edges.append(edge(m0+i, value))
            rand_nums.append(value)
            adj[m0 + i][value] = 1
            adj[value][m0 + i] = 1
        nodes_added+=1
    g.adjacency_matrix = adj
    return g

def main():
    f1 = open('dataset.txt', 'w')
    f2 = open('f2.txt', 'w')
    f3 = open('f3.txt', 'w')

    print 'generated 1'
    g1 = generate_random_graph(1000, 0.05)
    print 'generated 2'
    # g2 = generate_random_graph(5000, 0.05)
    print 'generated 3'
    # g3 = generate_random_graph(10000, 0.05)

    print '1 degree_distribution'
    f1.write('degree_distribution\n')
    for i, v in enumerate(g1.get_degree_distribution()):
        f1.write('{} {}\n'.format(i, v))

    print '1 cumulative_degree_distribution'
    f1.write('cumulative_degree_distribution\n')
    for i, v in enumerate(g1.get_cumulative_degree_distribution()):
        f1.write('{} {}\n'.format(i, v))

    print '1 clustering_coefficient'
    f1.write('clustering_coefficient\n')
    f1.write('{}\n'.format(g1.get_clustering_coefficient()))

    # print '1 average_path_length'
    # f1.write('average_path_length\n')
    # f1.write('{}\n'.format(g1.get_average_path_length()))
    # f1.close()

    # print '2 degree_distribution'
    # f2.write('degree_distribution\n')
    # for i, v in enumerate(g2.get_degree_distribution()):
    #    f2.write('{} {}\n'.format(i, v))

    # print '2 cumulative_degree_distribution'
    # f2.write('cumulative_degree_distribution\n')
    # for i, v in enumerate(g2.get_cumulative_degree_distribution()):
    #     f2.write('{} {}\n'.format(i, v))

    # print '2 clustering_coefficient'
    # f2.write('clustering_coefficient\n')
    # f2.write('{}\n'.format(g2.get_clustering_coefficient()))

    # print '2 average_path_length'
    # f2.write('average_path_length\n')
    # f2.write('{}\n'.format(g2.get_average_path_length()))
    # f2.close()

    # print '3 degree_distribution'
    # f3.write('degree_distribution\n')
    # for i, v in enumerate(g3.get_degree_distribution()):
    #     f3.write('{} {}\n'.format(i, v))

    # print '3 cumulative_degree_distribution'
    # f3.write('cumulative_degree_distribution\n')
    # for i, v in enumerate(g3.get_cumulative_degree_distribution()):
    #     f3.write('{} {}\n'.format(i, v))

    # print '3 clustering_coefficient'
    # f3.write('clustering_coefficient\n')
    # f3.write('{}\n'.format(g3.get_clustering_coefficient()))

    # print '3 average_path_length'
    # f3.write('average_path_length\n')
    # f3.write('{}\n'.format(g3.get_average_path_length()))
    # f3.close()

if __name__ == '__main__':
    main()
