import numpy as np
import os
import networkx as nx
import matplotlib.pyplot as plt
import warnings


def karate():
    # Read the network from a GML file
    def read_net_gml(file_name):
        if not os.path.exists(file_name):
            print(f"Error: The file '{file_name}' does not exist.")
            return None

        try:
            G = nx.read_gml(file_name, label='id')  # use 'id' as label if 'label' is missing

            # Assign default labels to nodes missing the 'label' attribute
            for node in G.nodes:
                if 'label' not in G.nodes[node]:
                    G.nodes[node]['label'] = node

            # Remove self-loops
            G.remove_edges_from(nx.selfloop_edges(G))

            return G
        except nx.NetworkXError as e:
            print("An error occurred while reading the GML file:", e)
            return None

    # Plot the network
    def plot_network(G):
        if G is None:
            print("Error: The network is empty.")
            return

        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 8))  # image is 8 x 8 inches
        nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        plt.show()

    # Plot a particular division into communities
    def plot_community_partition(G, communities):
        if G is None:
            print("Error: The network is empty.")
            return

        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 8))  # image is 8 x 8 inches

        # Create a list of colors for each node based on its community
        node_colors = [communities[node] for node in G.nodes]

        nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=node_colors)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        plt.show()

    # Evaluate the modularity of a partition
    def modularity(communities, G):
        if G is None:
            print("Error: The network is empty.")
            return None

        noNodes = len(G.nodes)
        degrees = dict(G.degree())
        noEdges = len(G.edges)
        M = 2 * noEdges
        Q = 0.0
        for i in G.nodes:
            for j in G.nodes:
                if communities[i] == communities[j]:
                    if G.has_edge(i, j):
                        Q += 1 - (degrees[i] * degrees[j]) / M
                    else:
                        Q -= (degrees[i] * degrees[j]) / M if M != 0 else 0  # Avoid division by zero
        return Q * 1 / M if M != 0 else 0  # Avoid division by zero

    # Detect communities using the greedy modularity algorithm
    def detect_communities(G):
        from networkx.algorithms.community import greedy_modularity_communities
        communities = list(greedy_modularity_communities(G))
        return communities

    # Assign community labels to nodes
    def assign_community_labels(G, communities):
        community_dict = {}
        for community_index, community in enumerate(communities):
            for node in community:
                community_dict[node] = community_index
        return community_dict

    # Load the network from the GML file
    crt_dir = os.getcwd()
    file_path = os.path.join(crt_dir, 'karate', 'karate.gml')
    network = read_net_gml(file_path)

    if network is None:
        print("Error: The network could not be loaded.")
        return

    # Detect communities
    communities = detect_communities(network)

    # Print the number of communities
    num_communities = len(communities)
    print("Number of communities identified:", num_communities)

    # Assign community labels to nodes
    community_labels = assign_community_labels(network, communities)

    # Print the community of each node
    for node, community in community_labels.items():
        print(f"Node {node} belongs to community {community}")

    # Plot the network
    warnings.simplefilter('ignore')
    plot_network(network)

    # Plot the community partition
    plot_community_partition(network, community_labels)

    # Evaluate modularity for the detected communities
    mod = modularity(community_labels, network)
    print("Modularity:", mod)

