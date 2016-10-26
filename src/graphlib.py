#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import networkx as nx
from Queue import Queue



    def calc_apl(adj):
        num_nodes = len(self.adj)
        num_pairs = 0
        total_length = 0
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j:
                    num_pairs += 1
                    total_length += self.bfs(i, j)
        return float(total_length) / float(num_pairs)

    def bfs(adj, orig, dest):
        size = len(self.adj)
        queue = Queue()
        visited = [0 for i in range(size)]

        dist = [0 for i in range(size)]

        visited[orig] = 1
        queue.put(orig)

        dist[orig] = 0

        while queue.empty() == False:
            aux = queue.get()

            for u in range(size):
                if self.adj[aux][u] == 1:
                    if visited[u] == 0:
                        dist[u] = dist[aux] + 1
                        queue.put(u)
                        visited[u] = 1
        return dist[dest]


def print_2d_array(array):
    print('[print_2dim_array]')
    n = len(array)
    for i in range(n):
        for j in range(n):
            print(array[i][j], end=' ')
        print('')


def main():


    adj = read_file()


    average_path_length = stats.calc_apl(adj.get_adjacency_matrix())


    print('Average path length:', average_path_length)


def read_file():
    g = nx.read_gml('input/adjnoun.gml')
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
