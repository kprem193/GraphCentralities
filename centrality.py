import networkx as nx
g = nx.read_edgelist("facebook_combined.txt",create_using=nx.Graph(), nodetype = int)
print(nx.info(g))

d=nx.degree_centrality(g)
d = sorted(d.items(), key=lambda x: x[1])
print(d, file=open("degreeCentrality.txt", "w"))

d=nx.betweenness_centrality(g, k=None, normalized=True, weight=None, endpoints=False, seed=None)
d = sorted(d.items(), key=lambda x: x[1])
print(d, file=open("betweennessCentrality.txt", "w"))

d=nx.closeness_centrality(g, u=None, distance=None, wf_improved=True, reverse=False)
d = sorted(d.items(), key=lambda x: x[1])
print(d, file=open("closenessCentrality.txt", "w"))

d=nx.eigenvector_centrality(g, max_iter=100, tol=1e-06, nstart=None, weight=None)
d = sorted(d.items(), key=lambda x: x[1])
print(d, file=open("eigenVectorCentrality.txt", "w"))