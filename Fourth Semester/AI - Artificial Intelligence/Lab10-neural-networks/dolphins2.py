import os
import networkx as nx
import matplotlib.pyplot as plt
import random
import warnings


def dolphins2():
    def read_net_gml(file_name):
        G = nx.read_gml(file_name)
        G.remove_edges_from(nx.selfloop_edges(G))  # Remove self-loops
        return G

    def plot_network(G):
        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 8))  # image is 8 x 8 inches
        nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        plt.show()

    def plot_community_partition(G, communities):
        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 8))  # image is 8 x 8 inches
        node_colors = [communities[node] for node in G.nodes]
        nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=node_colors)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
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

    def fitness_modularity(individual, G):
        mod = modularity(individual, G)
        num_communities = len(set(individual.values()))
        return mod - 0.1 * num_communities

    def fitness_community_density(individual, G):
        # calculeaza densitatea unui subgraf, nr muchii existente in subgraf / nr muchii posibile
        def density(subgraph):
            nodes = len(subgraph.nodes)
            if nodes <= 1:
                return 0
            possible_edges = nodes * (nodes - 1) / 2
            actual_edges = len(subgraph.edges)
            return actual_edges / possible_edges

        communities = {}
        for node, community in individual.items():
            if community not in communities:
                communities[community] = []
            communities[community].append(node)

        total_density = 0
        for community_nodes in communities.values():
            subgraph = G.subgraph(community_nodes)
            total_density += density(subgraph)

        num_communities = len(communities)
        return total_density / num_communities if num_communities != 0 else 0

    def fitness_community_clustering(individual, G):
        # calculeaza coeficientul mediu de clustering al unui subgraf Coeficientul de clustering al unui nod este
        # proportia de muchii intre vecinii sai din nr total de muchii posibile intre acestia
        def average_clustering(subgraph):
            if len(subgraph.nodes) == 0:
                return 0
            return nx.average_clustering(subgraph)

        communities = {}
        for node, community in individual.items():
            if community not in communities:
                communities[community] = []
            communities[community].append(node)

        # calculeaza subgraful pentru fiecare comunitate si aduna coeficientul de clustering al fiecaruia
        total_clustering = 0
        for community_nodes in communities.values():
            subgraph = G.subgraph(community_nodes)
            total_clustering += average_clustering(subgraph)

        num_communities = len(communities)
        return total_clustering / num_communities if num_communities != 0 else 0

    # selecteaza cei mai buni indivizi din populatie pe baza unei functii de fitness

    def selection(population, G, fitness_function):
        population.sort(key=lambda ind: fitness_function(ind, G), reverse=True)
        return population[:len(population) // 2]

    def crossover(parent1, parent2):
        child = parent1.copy()
        for key in parent2.keys():
            if random.random() > 0.5:
                child[key] = parent2[key]
        return child

# modifica un individ prin schimbarea comunitatii unui nod cu o probabilitate data

    def mutate(individual, mutation_rate):
        for key in individual.keys():
            if random.random() < mutation_rate:
                individual[key] = random.randint(0, 3)

    def genetic_algorithm(G, pop_size, generations, mutation_rate, fitness_function):
        population = initial_population(G, pop_size)
        for generation in range(generations):

            selected = selection(population, G, fitness_function)
            new_population = []
            while len(new_population) < pop_size:
                parent1, parent2 = random.sample(selected, 2)
                child = crossover(parent1, parent2)
                mutate(child, mutation_rate)
                new_population.append(child)
            population = new_population
        best_individual = max(population, key=lambda ind: fitness_function(ind, G))
        return best_individual

    # Load the network from the GML file
    crt_dir = os.getcwd()
    file_path = os.path.join(crt_dir, 'dolphins', 'dolphins.gml')
    network = read_net_gml(file_path)
    if network is None:
        print("Error: The network could not be loaded.")
        return

    # Choose the fitness function
    print("Choose the fitness function:")
    print("1. Modularity")
    print("2. Community Density")
    print("3. Community Clustering")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        fitness_function = fitness_modularity
    elif choice == '2':
        fitness_function = fitness_community_density
    elif choice == '3':
        fitness_function = fitness_community_clustering
    else:
        print("Invalid choice.")
        return

    # Run genetic algorithm to detect communities
    pop_size = 100
    generations = 200
    mutation_rate = 0.005
    best_community_partition = genetic_algorithm(network, pop_size, generations, mutation_rate, fitness_function)

    # Assign community labels to nodes
    community_labels = best_community_partition

    # Calculate the number of unique communities
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

    # Evaluate the chosen fitness function for the detected communities
    fitness_value = fitness_function(community_labels, network)
    print(f"Fitness value for the chosen function: {fitness_value}")
