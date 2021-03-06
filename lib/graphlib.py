#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import random
from Queue import Queue
import sys
class graph(object):
    """
    graph class

    Atributes:
        nodes (array:node): list of all the nodes of the graph.
        adjacency_matrix (array:array:int): adjacency matrix of the graph.
        degree_distribution (array:float): degree distribution of the graph.
        cumulative_degree_distribution (array:float): cumulative degree distribution of the graph.
        node_degree_histogram (array:int): node degree histogram of the graph.
        max_node_degree (int): max node degree of the graph.
        average_path_length (float): average path length of the graph.
        clustering_coefficient (float): clustering coefficient of the graph

    Methods:
        get_nodes (array:node): returns the list of all nodes of the graph.
        get_adjacency_matrix (array:array:int): returns the adjacency matrix of the graph.
        get_degree_distribution (array:floats): returns the degree distribution of the graph.
        get_cumulative_degree_distribution (array:floats): returns the cumulative degree distribution of the graph.
        get_node_degree_histogram (array:int): returns the node degree histogram of the graph.
        get_max_node_degree (int): returns the max node degree of the graph.
        calc_node_degrees (float): calculates all the node degrees and returns the average node degree of the graph.
        get_average_path_length (float): returns the average path length of the graph.
        get_clustering_coefficient (float): returns the clustering coefficient of the graph.
    """

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
        total = 0
        for node in self.nodes:
            total += node.get_node_degree()

        return float(total)/len(self.nodes)


    def get_average_path_length(self):
        if hasattr(self, 'average_path_length'):
            return self.average_path_length
        else:
            num_nodes = len(self.nodes)
            num_pairs = 0
            total_length = 0
            adj = self.get_adjacency_matrix()
            dist = floyd_warshall(adj)
            for i in range(num_nodes):
                for j in range(i, num_nodes):
                    if i != j:
                        if(dist[i][j]!=sys.maxint):
                            num_pairs += 1
                            total_length += dist[i][j]
            self.average_path_length = float(total_length) / num_pairs
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
                    self.adjacency_matrix[ edge.target ][ edge.source ] = 1
            return self.adjacency_matrix



    def __init__(self):
        self.nodes = []

class node(object):
    """
    node class

    Atributes:
        label (string): label of the node
        edges (array:edge): list all edges of the node
        degree (int): node degree
        clustering_coefficient (float): clustering coefficient of the node

    Methods:
        get_edges (array:edge): returns the list of all the node's edges
        get_node_degree (int): returns the node degree
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

    Atributes:
        source (int): index of the source node in the graph list of nodes
        target (int): index of the target node in the graph list of nodes

    Methods:
        get_source (int): returns the index of the source node in the graph list
        get_target (int): returns the index of the target node in the graph list
    """

    def get_source(self):
        return self.source

    def get_target(self):
        return self.target

    def __init__(self, source, target):
        super(edge, self).__init__()
        self.source = source
        self.target = target

def floyd_warshall(adj):
    num_nodes = len(adj)
    dist = [[sys.maxint for i in range(num_nodes)] for j in range(num_nodes)]

    for  i in range(num_nodes):
       dist[i][i] = 0

    for i in range(num_nodes):
        for j in range(num_nodes):
            if(adj[i][j]==1):
                dist[i][j] = 1

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if(dist[i][k]!=sys.maxint and dist[k][j]!=sys.maxint):
                    if(dist[i][j] > dist[i][k]+dist[k][j]):
                        dist[i][j] = dist[i][k] + dist[k][j]

    return dist



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
    f = nx.read_gml(file, label='id')
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
        for j in range(i, num_nodes):
            if(i!=j):
                if(random.random()<prob):
                    g.nodes[i].edges.append( edge(i, j) )
                    g.nodes[j].edges.append( edge(i, j) )
                    adj[i][j] = 1
                    adj[j][i] = 1
    g.adjacency_matrix = adj
    return g

def generate_minimal_graph(num_initial_nodes, num_nodes):
    e = []
    g = graph()

    g.nodes.append( node( 'node 0' ) )
    for i in range(1, num_initial_nodes):
        n = node( 'node {}'.format(i) )
        for index, nod in enumerate(g.nodes):
            ed = edge(i, index)
            nod.edges.append( ed )
            n.edges.append( ed )
            e.append(ed)
        g.nodes.append( n )

    for i in range(num_nodes - num_initial_nodes):
        r = random.randint(0, len(e)-1)
        g.nodes.append( node( 'node {}'.format(i + num_initial_nodes) ) )
        ed = edge(i + num_initial_nodes, e[r].source)
        g.nodes[i + num_initial_nodes].edges.append( ed )
        g.nodes[e[r].source].edges.append( ed )
        e.append(ed)
        ed = edge(i + num_initial_nodes, e[r].target)
        g.nodes[i + num_initial_nodes].edges.append( ed )
        g.nodes[e[r].target].edges.append( ed )
        e.append(ed)
    return g
