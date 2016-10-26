#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import random


def create_random_graph(num_nodes, prob):
	adj = [[0 for i in range(num_nodes)] for j in range(num_nodes)]

	for i in range (num_nodes):
		for j in range(num_nodes):
			if(i!=j):
				if(random.random()<prob):
					adj[i][j] = 1
					adj[j][i] = 1


def main():
	num_nodes = 20
	prob = 0.05
	create_random_graph(num_nodes, prob)
    
    

if __name__ == '__main__':
    main()
