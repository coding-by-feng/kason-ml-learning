"""
This module demonstrates the use of NetworkX for analyzing citation networks.
It creates a directed graph from citation data and performs basic network analysis.
"""
# pylint: disable=import-error
import networkx as nx
import pandas as pd
import os

# Define the path to the citation data file
citation_file = 'Pubmed-Diabetes.DIRECTED.cites.tab'

# Check if the file exists
if not os.path.exists(citation_file):
    print(f"Warning: File '{citation_file}' not found.")
    print("Creating a sample graph for demonstration purposes.")
    # Create a sample graph for demonstration
    G = nx.DiGraph()
    # Add some sample nodes and edges
    for i in range(1, 11):
        for j in range(i+1, min(i+4, 11)):
            G.add_edge(f"paper_{i}", f"paper_{j}")
else:
    # Load citation data from tab-separated file
    citations = pd.read_csv(citation_file, sep='\t')

    # Create a directed graph
    G = nx.DiGraph()

    # Add edges (citations) to the graph
    for _, row in citations.iterrows():
        G.add_edge(row['citing_paper_id'], row['cited_paper_id'])

# Basic network analysis
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

# Find most cited papers
most_cited = sorted(G.in_degree(), key=lambda x: x[1], reverse=True)[:10]
print("Most cited papers:", most_cited)
