import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph for data flow
G_data_flow = nx.DiGraph()

# Add nodes and edges for the modules
modules_data_flow = ["DataLoader", "MongoDB", "ItemCFRecommender", "OfflineRecommender", "OnlineRecommender", "Kafka", "StatisticsRecommender"]
edges_data_flow = [
    ("DataLoader", "MongoDB"),
    ("MongoDB", "ItemCFRecommender"),
    ("MongoDB", "OfflineRecommender"),
    ("ItemCFRecommender", "MongoDB"),
    ("OfflineRecommender", "MongoDB"),
    ("OnlineRecommender", "Kafka"),
    ("Kafka", "OnlineRecommender"),
    ("OnlineRecommender", "MongoDB"),
    ("StatisticsRecommender", "MongoDB")
]

G_data_flow.add_nodes_from(modules_data_flow)
G_data_flow.add_edges_from(edges_data_flow)

# Draw the data flow diagram
plt.figure(figsize=(10, 6))
pos_data_flow = nx.spring_layout(G_data_flow)
nx.draw(G_data_flow, pos_data_flow, with_labels=True, node_size=2000, node_color='lightgreen', font_size=10, font_weight='bold', edge_color='black')
plt.title("Data Flow Diagram")
plt.show()
