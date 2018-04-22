# -*- coding: utf-8 -*-
import networkx as nx
from networkx.readwrite import json_graph
import json

#卫星网络，两个
SatG1=nx.random_regular_graph(1,2)
SatG2=nx.random_regular_graph(2,3)

#接入卫星，2个子网，每个子网有三个
InSatG1=nx.random_regular_graph(2,3)
InSatG2=nx.random_regular_graph(2,3)

#地面子网，两个网络，第一个网络有50个结点，第二个网络有40个结点
LandG1=nx.random_regular_graph(3,70)
LandG2=nx.random_regular_graph(3,90)

G=nx.Graph()#最后返回的一张大图


#写入结点序号信息
totalNumOfNodes=1
nodeArr=[]
edgeArr=[]
def writeInfoToGraph(totalNumOfNodes,G,cate):
    num=totalNumOfNodes
    for item in G:
        # G.node[item]['index']=totalNumOfNodes
        # G.node[item]['category']=cate
        nodeArr.append(item+totalNumOfNodes)
        num=num+1

    edgeTemp=G.edges
    for item in edgeTemp:
        tempArr=[]
        for tul in item:
            tempArr.append(tul+totalNumOfNodes)
        outTul=(tempArr[0],tempArr[1])
        edgeArr.append(outTul)
    return num

totalNumOfNodes=writeInfoToGraph(totalNumOfNodes,SatG1,1)
totalNumOfNodes=writeInfoToGraph(totalNumOfNodes,SatG2,2)
totalNumOfNodes=writeInfoToGraph(totalNumOfNodes,InSatG1,3)
totalNumOfNodes=writeInfoToGraph(totalNumOfNodes,InSatG2,4)
totalNumOfNodes=writeInfoToGraph(totalNumOfNodes,LandG1,5)
totalNumOfNodes=writeInfoToGraph(totalNumOfNodes,LandG2,6)
totalNumOfNodes=totalNumOfNodes-1

G.add_nodes_from(nodeArr)
G.add_edges_from(edgeArr)

for item in G:
    if item>0 and item<3:
        G.node[item]['category']=1
    elif item>=3 and item<6:
        G.node[item]['category']=2
    elif item>=6 and item<9:
        G.node[item]['category']=3
    elif item>=9 and item<12:
        G.node[item]['category']=4
    elif item>=12 and item<82:
        G.node[item]['category']=5
    elif item>=82:
        G.node[item]['category']=6
    else:
        pass

#到这里，还差需要添加6个子网之间的连接

#转换为json
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
    with open("/Users/siriusblack/PycharmProjects/complex_network/templates/test3.json","w") as file:
        json.dump(wirteData,file)
    print "Update complete"

writeFile(G)
print G.edges
print G.nodes(data=True)


#接下来进行对每一个子网对攻击，并返回指标