#!/usr/bin/python
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

def main():
	num_nodes = 20
	prob = 0.05
	create_random_graph(num_nodes, prob)
    
    

if __name__ == '__main__':
    main()
