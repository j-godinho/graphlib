import lib.graphlib as gl

def main():
    # Generate a random model graph with 250 nodes and
    # a probability of 0.05 of each node beeing conected
    g = gl.generate_random_graph(250, 0.05)

    # Print the clustering coefficient of the generated graph
    print g.get_clustering_coefficient()


if __name__ == '__main__':
    main()
