
from __future__ import print_function
import networkx as nx
from Queue import Queue

class Statistics(object):

    """docstring for node."""

    def __init__(self, adj):
        self.adj = adj


	def calc_apl(self):

		num_nodes = len(self.adj)
		num_pairs = 0
		total_length = 0
		for i in range (num_nodes):
			for j in range (num_nodes):
				if(i!=j):
					num_pairs+=1
					total_length+=bfs(self.adj, i, j)		
		return float(total_length)/float(num_pairs)

	def bfs(self, orig, dest):
		size = len(self.adj)
		queue = Queue()
		visited = [0 for i in range(size)]

		dist = [0 for i in range(size)]

		visited[orig] = 1
		queue.put(orig)

		dist[orig] = 0

		while(queue.empty()==False):
			aux = queue.get()

			for u in range (size):
				if(self.adj[aux][u]==1):
					if(visited[u]==0):
						dist[u] = dist[aux]+1
						queue.put(u)
						visited[u]=1
		return dist[dest]


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
	#define adjacency_matrix test and its size
	#adj = [[0,1,1,0,0,0],[1,0,0,1,0,0],[1,0,0,1,0,0], [0,1,1,0,1,1], [0,0,0,1,0,0], [0,0,0,1,0,0]]
	#n = 3;

	adj = read_file()
	
	stats = Statistics(adj)
	average_path_length=stats.calc_apl()
	#print matrixes for test
	#print_2d_array(adj)	

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
