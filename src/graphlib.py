
from __future__ import print_function
import networkx as nx
import Queue
class node(object):
    """docstring for node."""
    def __init__(self, arg):
        super(node, self).__init__()
        self.arg = arg


def print_3d_array(array):
	print("[print_3d_array]")
	n = len(array)
	for i in range (n):
		for j in range (n):
			print (array[i][j], end=" ")
		print ("")	

def print_2d_array(array):
	print("[print_2d_array]")
	n = len(array)
	for i in range(n):
		print(array[i], end=" ")
	print("")


def get_degrees(adjacency_matrix):
	n = len(adjacency_matrix)
	degrees_array = []
	for i in range(n):
		aux_count = 0 
		for j in range(n):
			if(adjacency_matrix[i][j] == 1):
				aux_count = aux_count + 1

		degrees_array.append(aux_count)
	return degrees_array

# def bfs(adjacency_matrix):

# 	num_nodes = len(adjacency_matrix)
# 	dist_matrix = [[[-1] for i in range(num_nodes)] for j in range(num_nodes)]
# 	print_3d_array(dist_matrix)
# 	for i in range (num_nodes):
# 		bfs_rec(0, i, adjacency_matrix, dist_matrix)
# 	return dist_matrix
# def bfs_rec(dist, node, adjacency_matrix, dist_matrix):
# 	num_nodes = len(adjacency_matrix)
# 	for i in range (num_nodes):
# 		if(dist_matrix[node][i]<=dist):
# 			if(adjacency_matrix[node][i]==1):
# 				if(dist_matrix[node][i]>-1 and dist<dist_matrix[node][i]):
# 					dist_matrix[node][i] = dist
# 				bfs_rec(dist+1, node, adjacency_matrix, dist_matrix)

def bfs(adjacency_matrix, orig, dest):
	queue = Queue()
	dist = 0




def main():
	#define adjacency_matrix test and its size
	adj = [[0,1,1],[1,0,1],[1,1,0]]
	#n = 3;

	#adj = read_file()
	#calculate degrees of nodes
	degrees_array = get_degrees(adj)
	
	dist_matrix = bfs(adj, 0, 1)

	#print matrixes for test
	print_3d_array(adj)	
	print_2d_array(degrees_array)

	print_3d_array(dist_matrix)

def read_file():
    g = nx.read_gml('input/adjnoun.gml')
    nodes = nx.nodes(g)
    size = nx.number_of_nodes(g)
    adj = [[0 for x in range(size)] for y in range(size)]
    for node in nodes:
        edges = nx.edges(g, node)
        for edge in edges:
            adj[ nodes.index(edge[0]) ][ nodes.index(edge[1]) ] = 1
    return adj


if __name__ == "__main__":
    main()
