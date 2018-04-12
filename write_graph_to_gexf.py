# -*- coding: utf-8 -*-  
import networkx as nx
import matplotlib.pyplot as plt
from pylab import mpl                           #解决中文显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei']    #指定默认字体
import numpy as np

G=nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1,2)
G.add_edge(1,3)
nx.write_gexf(G,'/Users/siriusblack/Desktop/complex_network/Complex-Network/format.gexf')