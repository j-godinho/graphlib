
from __future__ import print_function
import networkx as nx
from Queue import Queue
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


def calc_apl(adjacency_matrix):

	num_nodes = len(adjacency_matrix)
	num_pairs = 0
	total_length = 0
	for i in range (num_nodes):
		for j in range (num_nodes):
			if(i!=j):
				num_pairs+=1
				total_length+=bfs(adjacency_matrix, i, j)

					
	#print ("total_length:", total_length, "num_pairs:", num_pairs)
	return float(total_length)/float(num_pairs)

def bfs(adjacency_matrix, orig, dest):
	size = len(adjacency_matrix)
	queue = Queue()
	visited = [0 for i in range(size)]

	dist = [9999 for i in range(size)]

	visited[orig] = 1
	queue.put(orig)

	dist[orig] = 0

	while(queue.empty()==False):
		aux = queue.get()

		for u in range (size):
			if(adjacency_matrix[aux][u]==1):
				if(visited[u]==0):
					dist[u] = dist[aux]+1
					queue.put(u)
					visited[u]=1
	return dist[dest]


def main():
	#define adjacency_matrix test and its size
	#adj = [[0,1,1,0,0,0],[1,0,0,1,0,0],[1,0,0,1,0,0], [0,1,1,0,1,1], [0,0,0,1,0,0], [0,0,0,1,0,0]]
	#n = 3;

	adj = read_file()
	#calculate degrees of nodes
	degrees_array = get_degrees(adj)
	
	average_path_length=calc_apl(adj)
	#print matrixes for test
	#print_3d_array(adj)	
	#print_2d_array(degrees_array)

	#print the average path length
	print("Average path length:" ,  average_path_length)


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
