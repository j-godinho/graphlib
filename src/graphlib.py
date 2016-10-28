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

def print_1d_array(array):
    print('[print_1d_array]')
    n = len(array)
    for i in range(n):
        print(array[i], end=' ')
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

def barabasi_albert_model(m0,links, num_nodes):
    #initialization of the array with init_nodes ALL connected
    adj = [[0 for i in range(num_nodes+m0)] for j in range(num_nodes+m0)]
    

    #initialization of adj with random links betweem m0 nodes
    for i in range(m0):
        index = i
        while (index == i):
            index = random.randint(0, m0-1)
            
        adj[i][index] = 1
        adj[index][i] = 1

   # print_2d_array(adj)

    nodes_added = 0
    for i in range(num_nodes):
        rand_nums = []
        for k in range (links):   
            value = random.randint(0, m0+nodes_added)
            while(value in rand_nums):
                value = random.randint(0, m0 + nodes_added)
            
            rand_nums.append(value)
            adj[m0 + i][value] = 1
            adj[value][m0 + i] = 1
        nodes_added+=1




    #print_2d_array(adj)
    #print_1d_array(degrees)
    
    

    #print_2d_ array(adj)
             


def main():

    m0 = 4
    links = 2
    num_nodes = 500
    barabasi_albert_model(m0, links, num_nodes)
    


if __name__ == '__main__':
    main()
