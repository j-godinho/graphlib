#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx
import random
import networkx as nx
from Queue import Queue

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

def get_degree_distribution(adj):
    degrees_array = get_degrees(adj)
    max_degree = get_max_degree(degrees_array)
    histogram = create_histogram(degrees_array, max_degree)
    cum_degree_array = create_cum_degree(histogram)
    degree_dist = create_degree_dist(cum_degree_array, adj)
    return degree_dist

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

def random_graph(num_nodes, prob):
    adj = [[0 for i in range(num_nodes)] for j in range(num_nodes)]

    for i in range (num_nodes):
        for j in range(num_nodes):
            if(i!=j):
                if(random.random()<prob):
                    adj[i][j] = 1
    return adj

def main():
    #g = read_file('input/clustering.gml')
    
    num_nodes = 50;
    prob = 0.05
    adj = random_graph(num_nodes, prob)
    get_degree_distribution(adj);
    

    print "Average Path Lenght: " ,calc_apl(adj) 
    
    degree_dist = get_degree_distribution(adj)

    for i in range(len(degree_dist)):
        print degree_dist[i]



if __name__ == '__main__':
    main()







