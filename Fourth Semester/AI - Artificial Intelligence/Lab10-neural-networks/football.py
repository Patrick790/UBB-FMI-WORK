import os
import networkx as nx
import matplotlib.pyplot as plt
import warnings


def football():
    # Custom function to read and clean GML file
    def read_net_gml(file_name):

        with open(file_name, 'r') as file:
            lines = file.readlines()

        edges = set()
        nodes = {}

        in_edge_block = False
        node_id = None


        for line in lines:
            # Verifica daca linia curentă incepe cu "node" pentru a marca inceputul sau sfarsitul blocului de muchii
            if line.strip().startswith("node"):
                in_edge_block = False
            elif line.strip().startswith("edge"):
                in_edge_block = True
            elif in_edge_block:
                if line.strip().startswith("source"):
                    source = int(line.split()[1])  # Extrage sursa muchiei
                elif line.strip().startswith("target"):
                    target = int(line.split()[1])  # Extrage destinația muchiei
                    # Adauga muchia la mulțimea de muchii, asigurandu-se ca muchiile sunt unice si neorientate
                    edges.add((min(source, target), max(source, target)))
            else:
                # Verifica daca linia curenta conține informatii despre un nod
                if line.strip().startswith("id"):
                    node_id = int(line.split()[1])  # Extrage ID-ul nodului
                    nodes[node_id] = {}  # Inițializează un dicționar pentru a stoca atributele nodului
                elif line.strip().startswith("label"):
                    nodes[node_id]['label'] = line.split()[1].strip('"')
                elif line.strip().startswith("value"):
                    nodes[node_id]['value'] = int(line.split()[1])

        G = nx.Graph()
        # Adauga fiecare nod din dictionarul de noduri, impreuna cu atributele sale, in graf
        for node, attr in nodes.items():
            G.add_node(node, **attr)
        # Adauga toate muchiile din multimea de muchii în graf
        G.add_edges_from(edges)

        G.remove_edges_from(nx.selfloop_edges(G))

        return G

    def plot_network(G):
        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 8))  # image is 8 x 8 inches
        nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        labels = nx.get_node_attributes(G, 'label')
        nx.draw_networkx_labels(G, pos, labels)
        plt.show()

    def plot_community_partition(G, community_labels):
        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 8))

        node_colors = [community_labels[node] for node in G.nodes]

        nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=node_colors)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        labels = nx.get_node_attributes(G, 'label')
        nx.draw_networkx_labels(G, pos, labels)
        plt.show()

    def modularity(community_labels, G):
        noNodes = len(G.nodes)
        degrees = dict(G.degree())
        noEdges = len(G.edges)
        M = 2 * noEdges
        Q = 0.0
        for i in G.nodes:
            for j in G.nodes:
                if community_labels[i] == community_labels[j]:
                    if G.has_edge(i, j):
                        Q += 1 - (degrees[i] * degrees[j]) / M
                    else:
                        Q -= (degrees[i] * degrees[j]) / M if M != 0 else 0
        return Q * 1 / M if M != 0 else 0

    # Detect communities using the greedy modularity algorithm
    def detect_communities(G):
        from networkx.algorithms.community import greedy_modularity_communities
        if len(G.edges) == 0:
            print("The graph has no edges.")
            return []
        communities = list(greedy_modularity_communities(G))
        return communities

    # Assign community labels to nodes
    def assign_community_labels(G, communities):
        community_dict = {}
        for community_index, community in enumerate(communities):
            for node in community:
                community_dict[node] = community_index
        return community_dict

    crt_dir = os.getcwd()
    file_path = os.path.join(crt_dir, 'football', 'football.gml')
    network = read_net_gml(file_path)

    if network is None:
        print("Error: The network could not be loaded.")
        return

    communities = detect_communities(network)

    if not communities:
        print("No communities detected.")
        return


    num_communities = len(communities)
    print("Number of communities identified:", num_communities)

    # Assign community labels to nodes
    community_labels = assign_community_labels(network, communities)

    for node, community in community_labels.items():
        print(f"Node {node} ({network.nodes[node]['label']}) belongs to community {community}")

    # Plot the network
    warnings.simplefilter('ignore')
    plot_network(network)

    # Plot the community partition
    plot_community_partition(network, community_labels)

    # Evaluate modularity for the detected communities
    mod = modularity(community_labels, network)
    print("Modularity:", mod)


