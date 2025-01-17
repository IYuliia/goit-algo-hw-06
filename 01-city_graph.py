import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
G.add_nodes_from(stations)


edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), 
         ('D', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'C')]
G.add_edges_from(edges)


plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16)
plt.title('Транспортна мережа міста')
plt.show()
plt.close()


num_nodes = G.number_of_nodes()  
num_edges = G.number_of_edges()  
degrees = dict(G.degree())      

print("Станції:", stations) 
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"Станція {node}: Ступінь = {degree}")

