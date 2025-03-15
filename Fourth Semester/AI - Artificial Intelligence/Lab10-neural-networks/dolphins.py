import os
import networkx as nx
import matplotlib.pyplot as plt
import warnings


def dolphins():
    # Function to read the network from a GML file
    def read_net_gml(file_name):
        G = nx.read_gml(file_name)
        G.remove_edges_from(nx.selfloop_edges(G))  # Remove self-loops from the network
        return G

    # Function to plot the network
    def plot_network(G):
        pos = nx.spring_layout(G)  # Compute node positions using the spring layout algorithm
        plt.figure(figsize=(8, 8))
        nx.draw_networkx_nodes(G, pos, node_size=600,
                               cmap=plt.cm.RdYlBu)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        plt.show()  # Show the plot

    # Function to plot a particular division into communities
    def plot_community_partition(G, communities):
        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 8))

        # Create a list of colors for each node based on its community
        node_colors = [communities[node] for node in G.nodes]

        nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=node_colors)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        plt.show()  # Show the plot

    # Function to evaluate the modularity of a partition
    def modularity(communities, G):
        noNodes = len(G.nodes)
        degrees = dict(G.degree())
        noEdges = len(G.edges)
        M = 2 * noEdges  # Total number of possible edges in an undirected graph
        Q = 0.0  # Initialize modularity value

        # Iterate over all pairs of nodes in the network
        for i in G.nodes:
            for j in G.nodes:
                # Check if the nodes belong to the same community
                if communities[i] == communities[j]:
                    if G.has_edge(i, j):
                        Q += 1 - (degrees[i] * degrees[j]) / M
                    else:
                        Q -= (degrees[i] * degrees[j]) / M if M != 0 else 0
        return Q * 1 / M if M != 0 else 0

    # Function to detect communities using the greedy modularity algorithm
    def detect_communities(G):
        from networkx.algorithms.community import \
            greedy_modularity_communities
        if len(G.edges) == 0:
            print("The graph has no edges.")
            return []
        communities = list(greedy_modularity_communities(G))
        return communities

    # Function to assign community labels to nodes
    def assign_community_labels(G, communities):
        community_dict = {}
        for community_index, community in enumerate(communities):
            for node in community:
                community_dict[node] = community_index  # Assign community label to each node
        return community_dict

    # Load the network from the GML file
    crt_dir = os.getcwd()
    file_path = os.path.join(crt_dir, 'dolphins', 'dolphins.gml')
    network = read_net_gml(file_path)

    if network is None:
        print("Error: The network could not be loaded.")
        return

    # Detect communities in the network
    communities = detect_communities(network)

    if not communities:
        print("No communities detected.")
        return

    # Print the number of communities detected
    num_communities = len(communities)
    print("Number of communities identified:", num_communities)

    # Assign community labels to nodes
    community_labels = assign_community_labels(network, communities)

    # Print the community of each node
    for node, community in community_labels.items():
        print(f"Node {node} belongs to community {community}")

    # Plot the network
    warnings.simplefilter('ignore')  # Suppress warnings
    plot_network(network)

    # Plot the community partition
    plot_community_partition(network, community_labels)

    # Evaluate modularity for the detected communities
    mod = modularity(community_labels, network)
    print("Modularity:", mod)


