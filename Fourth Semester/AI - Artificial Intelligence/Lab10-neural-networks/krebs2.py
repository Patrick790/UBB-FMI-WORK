import os
import networkx as nx
import matplotlib.pyplot as plt
import random
import warnings


def krebs2():
    def read_net_gml(file_name):
        G = nx.read_gml(file_name)
        G.remove_edges_from(nx.selfloop_edges(G))  # Remove self-loops

        # Check if nodes have a 'label' attribute, if not assign node name as label
        for node in G.nodes:
            if 'label' not in G.nodes[node]:
                G.nodes[node]['label'] = str(node)

        return G

    def plot_network(G, communities=None):
        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 8))  # image is 8 x 8 inches
        nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        labels = nx.get_node_attributes(G, 'label')
        nx.draw_networkx_labels(G, pos, labels)
        plt.show()

    def plot_community_partition(G, communities):
        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 8))  # image is 8 x 8 inches
        node_colors = [communities[node] for node in G.nodes]
        nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=node_colors)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        labels = nx.get_node_attributes(G, 'label')
        nx.draw_networkx_labels(G, pos, labels)
        plt.show()

    def modularity(communities, G):
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
                        Q -= (degrees[i] * degrees[j]) / M if M != 0 else 0
        return Q * 1 / M if M != 0 else 0

    def initial_population(G, pop_size):
        population = []
        for _ in range(pop_size):
            individual = {node: random.randint(0, 3) for node in G.nodes}  # Limit initial communities to 4
            population.append(individual)
        return population

    def fitness(individual, G):
        mod = modularity(individual, G)
        num_communities = len(set(individual.values()))
        return mod - 0.1 * num_communities  # Penalize for too many communities

    def selection(population, G):
        population.sort(key=lambda ind: fitness(ind, G), reverse=True)
        return population[:len(population) // 2]

    def crossover(parent1, parent2):
        child = parent1.copy()
        for key in parent2.keys():
            if random.random() > 0.5:
                child[key] = parent2[key]
        return child

    def mutate(individual, mutation_rate):
        for key in individual.keys():
            if random.random() < mutation_rate:
                individual[key] = random.randint(0, 3)  # Limit communities during mutation

    def genetic_algorithm(G, pop_size, generations, mutation_rate):
        population = initial_population(G, pop_size)
        for generation in range(generations):
            selected = selection(population, G)
            new_population = []
            while len(new_population) < pop_size:
                parent1, parent2 = random.sample(selected, 2)
                child = crossover(parent1, parent2)
                mutate(child, mutation_rate)
                new_population.append(child)
            population = new_population
        best_individual = max(population, key=lambda ind: fitness(ind, G))
        return best_individual

    # Load the network from the GML file
    crt_dir = os.getcwd()
    file_path = os.path.join(crt_dir, 'krebs', 'krebs.gml')
    network = read_net_gml(file_path)
    if network is None:
        print("Error: The network could not be loaded.")
        return

    # Run genetic algorithm to detect communities
    pop_size = 100
    generations = 200
    mutation_rate = 0.005
    best_community_partition = genetic_algorithm(network, pop_size, generations, mutation_rate)

    # Assign community labels to nodes
    community_labels = best_community_partition

    # Calculate the number of unique communities
    num_communities = len(set(community_labels.values()))
    print("Number of communities identified:", num_communities)

    # Print the community of each node
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

