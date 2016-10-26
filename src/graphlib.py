#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import networkx as nx


def create_histogram(degrees_array, max_degree):
    histogram = [0 for j in range(max_degree + 1)]
    n = len(degrees_array)
    for i in range(n):
        histogram[degrees_array[i]] += 1
    return histogram

def create_cum_degree(histogram):
    n = len(histogram)
    cum_degree_array = [0 for j in range(n)]
    for i in range(n):
        for j in range(i, n):
            cum_degree_array[i] += histogram[j]
    return cum_degree_array

def create_degree_dist(cum_degree_array, adj):
	n = len(cum_degree_array)
	num_nodes = len(adj)
	degree_dist = [float(cum_degree_array[i])/num_nodes for i in range(n)]
	return degree_dist

def get_max_degree(degrees_array):
    n = len(degrees_array)
    max_value = degrees_array[0]
    for i in range(1, n):
        if degrees_array[i] > max_value:
            max_value = degrees_array[i]
    return max_value

def get_degrees(adj):
    n = len(adj)
    degrees_array = []
    for i in range(n):
        aux_count = 0
        for j in range(n):
            if adj[i][j] == 1:
                aux_count = aux_count + 1
        degrees_array.append(aux_count)
    return degrees_array

def print_degree_dist(array):
    n = len(array)
    for i in range(n):
        print(array[i], end=' ')
    print('')

def get_degree_distribution(adj):
    degrees_array = get_degrees(adj)
    max_degree = get_max_degree(degrees_array)
    histogram = create_histogram(degrees_array, max_degree)
    cum_degree_array = create_cum_degree(histogram)
    degree_dist = create_degree_dist(cum_degree_array, adj)

    print_degree_dist(degree_dist)




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
            for node in self.nodes:
                size = len(self.nodes)
                k = node.get_node_degree()
                c_matrix = [[0 for x in range(size)] for y in range(size)]
                e = 0
                for edge in node.edges:
                    if c_matrix[edge.source][edge.target] == 0:
                        c_matrix[edge.source][edge.target] = 1
                        c_matrix[edge.target][edge.source] = 1
                        e += 1
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
    adj = read_file()
    
    #get_degree_distribution(adj.get_adjacency_matrix())


if __name__ == '__main__':
    main()
