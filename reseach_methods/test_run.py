import sys
with open('reseach_methods/test_output.txt', 'w') as f:
    try:
        import networkx as nx
        f.write("Successfully imported networkx\n")
    except ImportError as e:
        f.write(f"Error importing networkx: {e}\n")

    try:
        import pandas as pd
        f.write("Successfully imported pandas\n")
    except ImportError as e:
        f.write(f"Error importing pandas: {e}\n")

    try:
        # Try to read the file
        citations = pd.read_csv('Pubmed-Diabetes.DIRECTED.cites.tab', sep='\t')
        f.write("Successfully read the file\n")
    except Exception as e:
        f.write(f"Error reading file: {e}\n")
