import numpy as np
import os
import networkx as nx
import matplotlib.pyplot as plt
import warnings
import random


def karate2():
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

    # Genetic algorithm components
    def initialize_population(G, pop_size):
        population = []
        for _ in range(pop_size):
            individual = {node: random.randint(0, 3) for node in G.nodes}  # Limit initial communities to 4
            population.append(individual)
        return population

    def fitness(individual, G):
        mod = modularity(individual, G)
        num_communities = len(set(individual.values()))
        return mod - 0.1 * num_communities  # Penalize for too many communities

    def select_parents(population, fitnesses, num_parents):
        if all(fitness <= 0 for fitness in fitnesses):
            return random.sample(population, k=num_parents)
        else:
            min_fitness = min(fitnesses)
            adjusted_fitnesses = [f - min_fitness + 1 for f in fitnesses]  # Ensure all weights are positive
            return random.choices(population, weights=adjusted_fitnesses, k=num_parents)

    def crossover(parent1, parent2):
        cross_point = np.random.randint(1, len(parent1) - 1)
        child1 = parent1.copy()
        child2 = parent2.copy()
        for i, node in enumerate(list(parent1.keys())[cross_point:], start=cross_point):
            child1[node], child2[node] = parent2[node], parent1[node]
        return child1, child2

    def mutate(individual, mutation_rate):
        for node in individual.keys():
            if random.random() < mutation_rate:
                individual[node] = random.randint(0, 3)  # Limit communities during mutation
        return individual

    def genetic_algorithm(G, pop_size=100, num_generations=200, mutation_rate=0.01):
        population = initialize_population(G, pop_size)
        for generation in range(num_generations):
            fitnesses = [fitness(ind, G) for ind in population]
            parents = select_parents(population, fitnesses, pop_size // 2)
            next_population = []
            for i in range(0, len(parents), 2):
                parent1, parent2 = parents[i], parents[(i + 1) % len(parents)]
                child1, child2 = crossover(parent1, parent2)
                next_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
            population = next_population
            fitnesses = [fitness(ind, G) for ind in population]
            best_individual = population[np.argmax(fitnesses)]
        return best_individual

    # Assign community labels to nodes
    def assign_community_labels(individual, G, node_list):
        community_dict = {node: individual[node] for node in node_list}
        return community_dict

    # Load the network from the GML file
    crt_dir = os.getcwd()
    file_path = os.path.join(crt_dir, 'karate', 'karate.gml')
    network = read_net_gml(file_path)

    if network is None:
        print("Error: The network could not be loaded.")
        return

    # Create a list of nodes and a mapping to indices
    node_list = list(network.nodes)
    node_index_map = {node: i for i, node in enumerate(node_list)}

    # Detect communities using the genetic algorithm
    best_individual = genetic_algorithm(network)
    community_labels = assign_community_labels(best_individual, network, node_list)

    # Print the number of communities
    num_communities = len(set(community_labels.values()))
    print("Number of communities identified:", num_communities)

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
