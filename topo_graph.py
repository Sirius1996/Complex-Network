# -*- coding: utf-8 -*-
import networkx as nx
from networkx.readwrite import json_graph
import json
import threading
import time


#卫星网络，两个
SatG1=nx.random_regular_graph(3,10)
SatG2=nx.random_regular_graph(3,12)

#接入卫星，2个子网，每个子网有三个
InSatG1=nx.random_regular_graph(3,30)
InSatG2=nx.random_regular_graph(3,40)

#地面子网，两个网络，第一个网络有70个结点，第二个网络有90个结点
LandG1=nx.random_regular_graph(3 ,100)
LandG2=nx.random_regular_graph(3,100)

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


def putSubInGraph(totalNumOfNodes):
    totalNumOfNodes=writeInfoToGraph(totalNumOfNodes,SatG1,1)
    totalNumOfNodes=writeInfoToGraph(totalNumOfNodes,SatG2,2)
    totalNumOfNodes=writeInfoToGraph(totalNumOfNodes,InSatG1,3)
    totalNumOfNodes=writeInfoToGraph(totalNumOfNodes,InSatG2,4)
    totalNumOfNodes=writeInfoToGraph(totalNumOfNodes,LandG1,5)
    totalNumOfNodes=writeInfoToGraph(totalNumOfNodes,LandG2,6)


    G.add_nodes_from(nodeArr)
    G.add_edges_from(edgeArr)
    G.add_edge(SatG1.number_of_nodes(),SatG1.number_of_nodes()+1)
    G.add_edge(SatG1.number_of_nodes()+SatG2.number_of_nodes(),SatG1.number_of_nodes()+SatG2.number_of_nodes()+1)
    G.add_edge(SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes(),SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes()+1)
    G.add_edge(SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes()+InSatG2.number_of_nodes(),SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes()+InSatG2.number_of_nodes()+1)
    G.add_edge(SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes()+InSatG2.number_of_nodes()+LandG1.number_of_nodes(),SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes()+InSatG2.number_of_nodes()+LandG1.number_of_nodes()+1)
    G.add_edge(SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes()+InSatG2.number_of_nodes(),SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes()+InSatG2.number_of_nodes()+LandG1.number_of_nodes()+1)


    for item in G:

        if item>0 and item<SatG1.number_of_nodes()+1:
            G.node[item]['category']=1
        elif item>=SatG1.number_of_nodes()+1 and item<SatG1.number_of_nodes()+SatG2.number_of_nodes()+1:
            G.node[item]['category']=2
        elif item>=SatG1.number_of_nodes()+SatG2.number_of_nodes()+1 and item<SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes()+1:
            G.node[item]['category']=3
        elif item>=SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes()+1 and item<SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes()+InSatG2.number_of_nodes()+1:
            G.node[item]['category']=4
        elif item>=SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes()+InSatG2.number_of_nodes()+1 and item<SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes()+InSatG2.number_of_nodes()+LandG1.number_of_nodes()+1:
            G.node[item]['category']=5
        elif item>=SatG1.number_of_nodes()+SatG2.number_of_nodes()+InSatG1.number_of_nodes()+InSatG2.number_of_nodes()+LandG1.number_of_nodes()+1:
            G.node[item]['category']=6
        else:
            pass
    
    writeFile()
    totalNumOfNodes=1
#到这里，还差需要添加6个子网之间的连接
#另外需要处理：删掉的结点

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

def writeFile():
    wirteData=transGtoJson(G)
    with open("/Users/siriusblack/PycharmProjects/complex_network/templates/test3.json","w") as file:
        json.dump(wirteData,file)
    print "Update complete"
#写入文件
# writeFile()
# print G.nodes


#网络性能指标
#接下来进行对每一个子网对攻击，并返回指标
def reachable_nodes(G,start):
    seen=set()                                  #一个空集
    stack=[start]                               #一个空栈，将start放入
    while stack:
        node=stack.pop()
        if node not in seen:
            seen.add(node)
            stack.extend(G.neighbors(node))     #将这个结点的全部邻居入栈
    return len(seen)                                 #seen最后即存放所有邻居结点

def is_connected(G):
    for start in G:
        reachable=reachable_nodes(G,start)
    return len(reachable)==len(G)

def usable(G):    
    #此函数能够保证遍历整张图
    #该指标为网络可用性指标
    loopsize=0          #连通子集的数量
    pointNum=0
    tag=1
    sum=0
    for start in G:
        reachable=reachable_nodes(G,start)
        temp=reachable
        float(temp)
        if tag<reachable:
            tag=tag+1
        else:
            tag=1
            loopsize=loopsize+1
            sum=sum+temp*(temp-1)
        pointNum=pointNum+1
    #print sum,loopsize,pointNum
    if (float(loopsize)*float(pointNum)*(float(pointNum)-1))!=0:
        if (float(loopsize)*float(pointNum)*(float(pointNum)-1))==1.0:
            return float(sum)/(float(loopsize)*float(pointNum)*(float(pointNum)-1))*10
        else:
            return float(sum)/(float(loopsize)*float(pointNum)*(float(pointNum)-1))*1000
    else:
        return float(0)*100

def attack_func1(G,delNum):
    G.remove_node(delNum)
    transValToJson(usable(G))
    putSubInGraph(1)
    print usable(G)  

def attack_func2(G,delNum):
    score=nx.degree(G)
    score=sorted(score,key=lambda score:score[1],reverse=True)
    output=[]
    for node in score:
        output.append(node[0])
    print usable(G)
    transValToJson(usable(G))
    G.remove_node(delNum)
    transValToJson(usable(G))
    print usable(G)

def attack_func3(G,delNum):
    score = nx.betweenness_centrality(G)  
    score = sorted(score.items(), key=lambda item:item[1], reverse = True)  
    output = []  
    for node in score:  
        output.append(node[0])
    G.remove_node(delNum)
    transValToJson(usable(G))
    print usable(G)


def delNodeByTime(g,num):
    g.remove_node(num)

def transValToJson(val):
    inputData={'Num':val}
    with open("/Users/siriusblack/PycharmProjects/complex_network/templates/format2json.json","w") as file:
        json.dump(inputData,file)

# global delNodeCount
# delNodeCount=1
# for timerCount in range(1,250):
#     timeFun=threading.Timer(2,writeFile)
#     timeFun.start()
#     time.sleep(1)
#     delNodeCount=delNodeCount+1
#     timerCount=timerCount+1

# for i in range(1,150):
#     G.remove_node(i)
#     writeFile()
#     transValToJson(usable(G))
#     time.sleep(2)
#     print usable(G)

putSubInGraph(1)

#接下来：针对每个不同子网的攻击：用序号去处理
#处理完之后，重新写入整个大网
for i in range(1,40):
    attack_func1(LandG2,i)
    time.sleep(2)

