# Noodling around with networkx based on Chris's Day12.ipynb code. Learn by doing.
from utils import get_data_lines
import networkx as nx

if __name__ == '__main__':
    sample, full = get_data_lines(12)

    sample_graph = nx.parse_edgelist(sample, delimiter='-')
    full_graph = nx.parse_edgelist(full, delimiter='-')

    nx.nx_pydot.write_dot(sample_graph, '13s.dot')
    nx.nx_pydot.write_dot(full_graph, '13.dot')
