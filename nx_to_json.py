# -*- coding: utf-8 -*-
import networkx as nx
from networkx.readwrite import json_graph
import json


g = nx.Graph()

g.add_node(0, name='Node 1')
g.add_node(1, name='Node 2')
g.add_node(2, name='Node 3')
g.add_edge(0,1)
g.add_edge(1,2)
g.add_node(3)
g.add_node(4)
g.add_edge(3,4)

#构造一个有20个结点，每个节点度为3度规则分布网络测试显示
RG=nx.random_regular_graph(3,20)
pos = nx.spectral_layout(RG)


#转换成json处理
def transGtoJson(g):
    temp=json_graph.node_link_data(g)
    trans=json.dumps(temp)
    transArr=json.loads(trans)
    transNodes=transArr['nodes']
    transLinks=transArr['links']
    print transNodes
    print transLinks
    for item in transNodes:
        item['category']=1
    #封装json
    attributes_dict={'type':'force','categories':[{'name':'HTMLElement','keyword':{},'base':'HTMLElement'},{'name':'WebGL','keyword':{},'base':'WebGLRenderingContext'},{'name': 'SVG','keyword': {},'base': 'SVGElement'},{'name':'css','keyword':{},'base':'CSSRule'},{'name':'Other','keyword':{}}]}
    retArr=attributes_dict
    retArr['nodes']=transNodes
    retArr['links']=transLinks
    return retArr

wirteData=transGtoJson(RG)
print wirteData
with open("/Users/siriusblack/PycharmProjects/complex_network/templates/test2.json","w") as file:
    json.dump(wirteData,file)