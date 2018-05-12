# -*- coding: utf-8 -*-
import networkx as nx
import threading

G=nx.random_regular_graph(3,200)

exitFlag=0

def runFunc(item):
    G.remove_node(item)
    print "remove node",item

