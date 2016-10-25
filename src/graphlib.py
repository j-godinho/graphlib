#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import networkx as nx
from matplotlib import pyplot as plt


class Statistics(object):

    """docstring for node."""

    def __init__(self, adj):
        self.adj = adj

    def create_histogram(self, max_degree):
        histogram = [0 for j in range(max_degree + 1)]
        n = len(self.degrees_array)
        for i in range(n):
            histogram[self.degrees_array[i]] += 1
        return histogram

    def create_cum_degree(self):
        n = len(self.histogram)
        cum_degree_array = [0 for j in range(n)]
        for i in range(n):
            for j in range(i, n):
                cum_degree_array[i] += self.histogram[j]
        return cum_degree_array

    def create_degree_dist(self):
    	n = len(self.cum_degree_array)
    	num_nodes = len(self.adj)
    	degree_dist = [float(self.cum_degree_array[i])/num_nodes for i in range(n)]
    	return degree_dist

    def get_max_degree(self):
        n = len(self.degrees_array)
        max_value = self.degrees_array[0]
        for i in range(1, n):
            if self.degrees_array[i] > max_value:
                max_value = self.degrees_array[i]
        return max_value

    def get_degrees(self):
        n = len(self.adj)
        degrees_array = []
        for i in range(n):
            aux_count = 0
            for j in range(n):
                if self.adj[i][j] == 1:
                    aux_count = aux_count + 1
            degrees_array.append(aux_count)
        return degrees_array

    def create_statistics(self):
        self.degrees_array = self.get_degrees()
        max_degree = self.get_max_degree()
        self.histogram = self.create_histogram(max_degree)
        self.cum_degree_array = self.create_cum_degree()
        self.degree_dist = self.create_degree_dist()

        #plots


def print_2d_array(array):
    print('[print_2dim_array]')
    n = len(array)
    for i in range(n):
        for j in range(n):
            print(array[i][j], end=' ')
        print('')


def print_1d_array(array):
    print('[print_1dim_array]')
    n = len(array)
    for i in range(n):
        print(array[i], end=' ')
    print('')


def main():

    # define adjacency_matrix test and its size
    # adjacency_matrix = [[0,1,1],[1,0,1],[1,1,0]]
    # n = 3;

    adj = read_file()

    stats = Statistics(adj)
    stats.create_statistics()

    # print matrixes for test
    print_2d_array(stats.adj)
    print_1d_array(stats.degrees_array)
    print_1d_array(stats.histogram)
    print_1d_array(stats.cum_degree_array)
    print_1d_array(stats.degree_dist)

def read_file():
    g = nx.read_gml('../input/adjnoun.gml')
    nodes = nx.nodes(g)
    size = nx.number_of_nodes(g)
    adj = [[0 for x in range(size)] for y in range(size)]
    for node in nodes:
        edges = nx.edges(g, node)
        for edge in edges:
            adj[nodes.index(edge[0])][nodes.index(edge[1])] = 1
    return adj


if __name__ == '__main__':
    main()
