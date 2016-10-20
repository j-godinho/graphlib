from __future__ import print_function



def print_3d_array(array, n):
	print("[print_3d_array]")
	for i in range (n):
		for j in range (n):
			print (array[i][j], end=" ")
		print ("")	

def print_2d_array(array, n):
	print("[print_2d_array]")
	for i in range(n):
		print(array[i], end=" ")
	print("")

def build_histogram(degrees_array, n):
	histogram = [0 for j in range(n)]
	for i in range(n):
		histogram[degrees_array[i]]+=1
	return histogram

def get_max_degree(degrees_array, n):
	max_value = degrees_array[0]
	for i in range(1, n):
		if(degrees_array[i]>max_value):
			max_value = degrees_array[i]
	return max_value

def get_degrees(adjacency_matrix, n):
	degrees_array = []
	for i in range(n):
		aux_count = 0 
		for j in range(n):
			if(adjacency_matrix[i][j] == 1):
				aux_count = aux_count + 1

		degrees_array.append(aux_count)
	return degrees_array

def main():
	#define adjacency_matrix test and its size
	adjacency_matrix = [[0,1,1],[1,0,1],[1,1,0]]
	n = 3;

	#calculate degrees of nodes
	degrees_array = get_degrees(adjacency_matrix, n)

	#get the max degree of the list of degrees
	max_degree = get_max_degree(degrees_array, n)
	
	#build the histogram relative to the list of degrees
	histogram = build_histogram(degrees_array, n)

	#print matrixes for test
	print_3d_array(adjacency_matrix, n)	
	print_2d_array(degrees_array, n)
	print_2d_array(histogram, n)

if __name__ == "__main__":
    main()
