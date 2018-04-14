# -*- coding: utf-8 -*-
import networkx as nx
from networkx.readwrite import json_graph
import json


g = nx.Graph()

g.add_node('N1', name='Node 1')
g.add_node('N2', name='Node 2')
g.add_node('N3', name='Node 3')
g.add_edge('N1', 'N2')
g.add_edge('N1', 'N3')

#转换成json处理
def transGtoJson(g):
    temp=json_graph.node_link_data(g)
    trans=json.dumps(temp)
    # print trans
    transArr=json.loads(trans)
    transNodes=transArr['nodes']
    transLinks=transArr['links']
    # a=json.dumps(transNodes)
    # b=json.dumps(transLinks)
    # print a,b
    #封装json
    attributes_dict={'type':'force','categories':[{'name':'HTMLElement','keyword':{},'base':'HTMLElement'},{'name':'WebGL','keyword':{},'base':'WebGLRenderingContext'},{'name': 'SVG','keyword': {},'base': 'SVGElement'},{'name':'css','keyword':{},'base':'CSSRule'},{'name':'Other','keyword':{}}]}
    # print attributes_dict
    retArr=attributes_dict
    retArr['nodes']=transNodes
    retArr['links']=transLinks
    ret=json.dumps(retArr)
    print ret

transGtoJson(g)