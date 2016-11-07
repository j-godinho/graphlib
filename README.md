#graphlib.py
graphlib.py is a simple Python library made as a project to our Masters course at IST in Lisbon. 

##Generating a Graph 
There are two possible ways of generating a graph in our library. You can either 
 input a `.gml` file or you can use one of our random graph models implemented.

```python
g = read_file(path_to_file)
```
or using any of the models implemented:

```python
g = generate_random_graph(number_of_nodes, prob)
g = generate_minimal_graph(number_of_initial_nodes, number_of_nodes)
```
where `prob` is the probability of two nodes being connected.

##Random graph models

###Random model
In the random model we create a graph of n nodes, with a given probability of each node connect to any of the others.

###Minimal model
In the minimal model a graph we begin by creating the initial nodes and connecting them to the rest of the nodes. Then we create `number_of_nodes - number_of_initial_nodes` following the rules:

1. Choose an existing edge
2. Connect the new node to both nodes of the edge

##Metrics implemented
1. Degree Distribution 
2. Cumulative Degree Distribution
3. Average Path Length
4. Clustering Coefficient


##Reference

###graph class
`get_nodes() array:int` - returns the list of nodes

`get_adjacency_matrix() array:array:int` - returns the adjacency matrix of the graph.

`get_degree_distribution() array:float` - returns the degree distribution of the graph.

`get_cumulative_degree_distribution array:float` - returns the cumulative degree distribution of the graph.

`get_node_degree_histogram array:int` - returns the node degree histogram of the graph.

`get_max_node_degree int` - returns the max node degree of the graph.

`calc_node_degrees float` - calculates all the node degrees and returns the average node degree of the graph.

`get_average_path_length float` - returns the average path length of the graph.

`get_clustering_coefficient float` - returns the clustering coefficient of the graph.

###node class
`get_edges() array:edge` - returns the list of all the node's edges

`get_node_degree() int` - returns the node degree

###edge class
`get_source() int` - returns the index of the source node in the graph list

`get_target() int` - returns the index of the target node in the graph lis

##Credits
We used the [networkx](http://networkx.github.io/) library to parse the `.gml` files.
