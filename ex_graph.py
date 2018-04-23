# -*- coding: utf-8 -*-  
import networkx as nx
import matplotlib.pyplot as plt
from pylab import mpl                           #解决中文显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei']    #指定默认字体
import numpy as np
from networkx.readwrite import json_graph
import json


G = nx.random_geometric_graph(200, 0.125)
pos = nx.get_node_attributes(G, 'pos')
dmin = 1
ncenter = 0
for n in pos:
    x, y = pos[n]
    d = (x - 0.5)**2 + (y - 0.5)**2
    if d < dmin:
        ncenter = n
        dmin = d

# color by path length from node near center

# plt.figure(figsize=(8, 8))
# nx.draw_networkx_edges(G, pos, nodelist=[ncenter], alpha=0.4)
# nx.draw_networkx_nodes(G, pos, nodelist=list(p.keys()),
#                        node_size=80,
#                        node_color=list(p.values()),
#                        cmap=plt.cm.Blues_r)

# plt.xlim(-0.05, 1.05)
# plt.ylim(-0.05, 1.05)
# plt.axis('off')
# plt.show()




#问题：如何确定队列长度以及每一次迭代后的位置
#解决方案：求补集，每一次返回一个补集，及上一集合的长度
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
    #print sum,loopsize,pointNum
    if (float(loopsize)*float(pointNum)*(float(pointNum)-1))!=0:
        return float(sum)/(float(loopsize)*float(pointNum)*(float(pointNum)-1))
    else:
        return float(0)

def attack_func1(G):
    graph_size=6
    print usable(G)
    for num in range(1,graph_size):
        G.remove_node(num)
        print usable(G)  

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

def attack_func3(G):
    score = nx.betweenness_centrality(G)  
    score = sorted(score.items(), key=lambda item:item[1], reverse = True)  
    output = []  
    for node in score:  
        output.append(node[1])  
    print(output)  


# print usable(G)


# degree=nx.degree_histogram(G)
# x = range(len(degree))                             #生成x轴序列，从1到最大度
# y = [z / float(sum(degree)) for z in degree]  
# plt.loglog(x,y,color="blue",linewidth=2)           #在双对数坐标轴上绘制度分布曲线  
# plt.show()  

# graph_size=200
# print usable(G)
# for num in range(1,graph_size):
#     G.remove_node(num)
#     print usable(G)

# attack_func2(G)
attack_func3(G)
