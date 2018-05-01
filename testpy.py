# -*- coding: utf-8 -*-
import networkx as nx
from networkx.readwrite import json_graph
import json


G=nx.random_regular_graph(3,20)

G.remove_node(3)

for item in range(1,G.number_of_nodes()+1):
    if G.has_node(item)==True:
        print "YES"
    else:
        print "NO"