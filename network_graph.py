# -*- coding: utf-8 -*-  
import networkx as nx
import matplotlib.pyplot as plt
from pylab import mpl                           #解决中文显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei']    #指定默认字体
import numpy as np

Int_Graph=nx.Graph()
# Int_Graph=nx.Graph()
# Int_Graph=nx.Graph()
# Sky_Graph2=nx.Graph()
# Land_Graph1=nx.Graph()
# Land_Graph2=nx.Graph()
# Land_Graph3=nx.Graph()

Int_Graph.add_node("S1")
Int_Graph.add_node("S2")
Int_Graph.add_node("SC")
Int_Graph.add_edge("S1","S2")
Int_Graph.add_edge("S1","SC")
Int_Graph.add_edge("S2","SC")


Int_Graph.add_node("K1")
Int_Graph.add_node("K2")
Int_Graph.add_node("K3")
Int_Graph.add_edge("K1","K2")
Int_Graph.add_edge("K2","K3")
Int_Graph.add_edge("K1","K3")

Int_Graph.add_node("K4")
Int_Graph.add_node("K5")
Int_Graph.add_node("K6")
Int_Graph.add_edge("K4","K5")
Int_Graph.add_edge("K4","K6")
Int_Graph.add_edge("K5","k6")

Int_Graph.add_edge("K1","SC")
Int_Graph.add_edge("K2","SC")
Int_Graph.add_edge("K4","SC")
Int_Graph.add_edge("K5","SC")
Int_Graph.add_edge("K6","SC")




#nx.draw(Int_Graph,pos=None, with_labels = True, node_size = 350)
#plt.show()

#网络可用性指标
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
    if (float(loopsize)*float(pointNum)*(float(pointNum)-1))!=0:
        return float(sum)/(float(loopsize)*float(pointNum)*(float(pointNum)-1))
    else:
        return float(0)

        

#代价下网络攻击实现


#1、采用随机方式生成初始解，初始顺序为默认顺序
def attack_func1(G):
    graph_size=6
    print usable(G)
    for num in range(1,graph_size):
        G.remove_node(num)
        print usable(G)  

#2、采用代价下的攻击方式：度数优先的攻击
#思路：嗅探结点度数，按照度数大小从大到小攻击
def attack_func2(G):
    score=nx.degree(G)
    score=sorted(score,key=lambda score:score[1],reverse=True)
    output=[]
    graph_size=6
    for node in score:
        output.append(node[0])
    print usable(G)
    for num in range(1,graph_size):
        G.remove_node(num)
        print usable(G)


#3、采用代价下的攻击方式：介数优先度攻击
#思路：按结点介数大小从大到小攻击
def attack_func3(G):
    score = nx.betweenness_centrality(G)  
    score = sorted(score.items(), key=lambda item:item[1], reverse = True)  
    output = [] 
    graph_size=6 
    for node in score:  
        output.append(node[0])  
    print usable(G)
    for num in range(1,graph_size):
        G.remove_node(num)
        print usable(G)


TG=nx.Graph()
TG.add_node(1)
TG.add_node(2)
TG.add_edge(1,2)
TG.add_node(3)
TG.add_node(4)
TG.add_node(5)
TG.add_edge(3,4)
TG.add_edge(4,5)
TG.add_node(6)

# nx.draw(TG , pos=None, with_labels = True, node_size = 350)
# plt.show()

attack_func2(TG)