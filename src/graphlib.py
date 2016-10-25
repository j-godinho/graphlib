#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import random


def print_2d_array(array):
    print('[print_2dim_array]')
    n = len(array)
    for i in range(n):
        for j in range(n):
            print(array[i][j], end=' ')
        print('')

def create_random_graph(num_nodes, prob):
	adj = [[0 for i in range(num_nodes)] for j in range(num_nodes)]

	for i in range (num_nodes):
		for j in range(num_nodes):
			if(i!=j):
				if(random.random()<prob):
					adj[i][j] = 1
					adj[j][i] = 1

	print_2d_array(adj)

def barabasi_albert_model(init_nodes, num_nodes, prob):
    #initialization of the array with init_nodes ALL connected
    adj = [[1 if i!=j else 0 for i in range(init_nodes)] for j in range(init_nodes)]
    print_2d_array(adj)

def main():

    init_nodes = 2
    num_nodes = 20
    prob = 0.05
    barabasi_albert_model(init_nodes,num_nodes, prob)
    


if __name__ == '__main__':
    main()
