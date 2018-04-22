#coding: utf-8  
#!/usr/bin/env python  
""" 
Draw a graph with matplotlib. 
You must have matplotlib for this to work. 
"""  
__author__ = """Aric Hagberg (hagberg@lanl.gov)"""  
#    Copyright (C) 2004-2008  
#    Aric Hagberg <hagberg@lanl.gov>  
#    Dan Schult <dschult@colgate.edu>  
#    Pieter Swart <swart@lanl.gov>  
#    All rights reserved.  
#    BSD license.  
#raise的使用要求这一步必须执行  
try:  
    import matplotlib.pyplot as plt  
except:  
    raise  
import networkx as nx  
#用grid_2d_graph()生成一个16个节点的网格图  
G=nx.grid_2d_graph(4,4)  #4x4 grid  
pos=nx.spring_layout(G,iterations=100)  
#开始画各个小图  
plt.subplot(221)  
nx.draw(G,pos,font_size=8)  
plt.subplot(222)  
nx.draw(G,pos,node_color='k',node_size=0,with_labels=False)  
plt.subplot(223)  
nx.draw(G,pos,node_color='g',node_size=250,with_labels=False,width=6)  
#最后一幅子图转为有向图  
plt.subplot(224)  
H=G.to_directed()  
nx.draw(H,pos,node_color='b',node_size=20,with_labels=False)  
plt.savefig("four_grids.png")  
plt.show()