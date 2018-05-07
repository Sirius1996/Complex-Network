# -*- coding: utf-8 -*-
import networkx as nx
from networkx.readwrite import json_graph
import json

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
        print reachable
    return reachable==len(G)

def usable(G,nodesNum):
    flag=0
    tempCount=1
    sumNum=0.0
    for i in G:
        if flag==0:
            sumNum=sumNum+reachable_nodes(G,i)*(reachable_nodes(G,i)-1)
            flag=1
            tempCount=tempCount+1
        elif flag==1:
            if tempCount==reachable_nodes(G,i):
                flag=0
                tempCount=1
            else:
                tempCount=tempCount+1
    return float(sumNum/(nodesNum*(nodesNum-1)))



def usable1(UG):
    #此函数能够保证遍历整张图
    #该指标为网络可用性指标
    loopsize=0          #连通子集的数量
    pointNum=0          #每个连通子集中点的数量
    tag=1
    sum=0
    for start in UG:
        reachable=reachable_nodes(UG,start)
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
            return float(sum)/(float(loopsize)*float(pointNum)*(float(pointNum)-1))
        else:
            return float(sum)/(float(loopsize)*float(pointNum)*(float(pointNum)-1))
    else:
        return 0


G=nx.random_regular_graph(3,200)
AG=nx.Graph()
AG.add_node(1)
AG.add_node(2)
AG.add_node(3)
AG.add_node(4)
AG.add_node(5)
AG.add_edge(1,2)
AG.add_edge(2,3)
AG.add_edge(4,5)
temp=AG.number_of_nodes()

score = nx.betweenness_centrality(AG)  
score = sorted(score.items(), key=lambda item:item[1], reverse = True)  
output = []  
for node in score:  
    output.append(node[0])
print output