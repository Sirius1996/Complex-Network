# -*- coding: utf-8 -*-
import networkx as nx
from networkx.readwrite import json_graph

from pyecharts import Graph

g = nx.Graph()

g.add_node('N1', name='Node 1')
g.add_node('N2', name='Node 2')
g.add_node('N3', name='Node 3')
g.add_edge('N1', 'N2')
g.add_edge('N1', 'N3')

g_data = json_graph.node_link_data(g)

print(g_data)

eg = Graph('设备最新拓扑图')
eg.add('Devices', nodes=g_data['nodes'], links=g_data['links'])
#eg.show_config()
eg.render()
