# -*- coding: utf-8 -*-
import networkx as nx
from networkx.readwrite import json_graph
import json


def transGtoJson(G):
    temp=json_graph.node_link_data(G)
    trans=json.dumps(temp)
    transArr=json.loads(trans)
    transNodes=transArr['nodes']
    transLinks=transArr['links']
    tempLinkArr=[]
    for items in transLinks:
        s=items['source']-1
        t=items['target']-1
        tempDict={u'source':s,u'target':t}
        tempLinkArr.append(tempDict)
    attributes_dict={'type':'force','categories':[{'name':'Web1','keyword':{},'base':'Web1'},{'name':'Web2','keyword':{},'base':'Web2'},{'name':'Web3','keyword':{},'base':'Web3'},{'name': 'Web4','keyword': {},'base': 'Web4'},{'name':'Web5','keyword':{},'base':'Web'},{'name':'Other','keyword':{}}]}
    retArr=attributes_dict
    retArr['nodes']=transNodes
    retArr['links']=tempLinkArr
    return retArr

def writeFile(G):
    wirteData=transGtoJson(G)
    with open("/Users/siriusblack/PycharmProjects/complex_network/templates/net6.json","w") as file:
        json.dump(wirteData,file)
    print "Update complete"

G1=nx.random_regular_graph(2,10)
G2=nx.random_regular_graph(3,10)
G3=nx.random_regular_graph(3,30)
G4=nx.random_regular_graph(3,40)
G5=nx.random_regular_graph(3,100)
G6=nx.random_regular_graph(4,100)
writeFile(G6)