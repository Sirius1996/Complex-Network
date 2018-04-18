# -*- coding: utf-8 -*-
import networkx as nx
from networkx.readwrite import json_graph
import json
import threading
import time


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

def attack_func1(G,delNum):
    print usable(G)
    transValToJson(usable(G))
    G.remove_node(delNum)
    transValToJson(usable(G))
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


#将图转换成json处理
def transGtoJson(g):
    temp=json_graph.node_link_data(g)
    trans=json.dumps(temp)
    transArr=json.loads(trans)
    transNodes=transArr['nodes']
    transLinks=transArr['links']
    # print transNodes
    # print transLinks
    for item in transNodes:
        item['category']=1
    #封装json
    attributes_dict={'type':'force','categories':[{'name':'HTMLElement','keyword':{},'base':'HTMLElement'},{'name':'WebGL','keyword':{},'base':'WebGLRenderingContext'},{'name': 'SVG','keyword': {},'base': 'SVGElement'},{'name':'css','keyword':{},'base':'CSSRule'},{'name':'Other','keyword':{}}]}
    retArr=attributes_dict
    retArr['nodes']=transNodes
    retArr['links']=transLinks
    return retArr

def delNodeByTime(g,num):
    g.remove_node(num)

def transValToJson(val):
    inputData={'Num':val}
    with open("/Users/siriusblack/PycharmProjects/complex_network/templates/format2json.json","w") as file:
        json.dump(inputData,file)



#构造一个有20个结点，每个节点度为3度规则分布网络测试显示
global RG,delNodeCount
delNodeCount=1
RG=nx.random_regular_graph(3,100)
pos = nx.spectral_layout(RG)

def writeFile():
    #delNodeByTime(RG,delNodeCount)
    attack_func3(RG,delNodeCount)
    wirteData=transGtoJson(RG)
    with open("/Users/siriusblack/PycharmProjects/complex_network/templates/test3.json","w") as file:
        json.dump(wirteData,file)
    print "Update complete"


for timerCount in range(1,50):
    timeFun=threading.Timer(2,writeFile)
    timeFun.start()
    time.sleep(5)
    delNodeCount=delNodeCount+1
    timerCount=timerCount+1

# g = nx.Graph()

# g.add_node(0, name='Node 1')
# g.add_node(1, name='Node 2')
# g.add_node(2, name='Node 3')
# g.add_edge(0,1)
# g.add_edge(1,2)
# g.add_node(3)
# g.add_node(4)
# g.add_edge(3,4)