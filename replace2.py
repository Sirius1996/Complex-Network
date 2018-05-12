# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import networkx as nx
from networkx.readwrite import json_graph
import json
import threading
import thread
import time
from django.http import JsonResponse

# Create your views here.
#卫星网络，两个
SatG11=nx.random_regular_graph(3,12)
SatG12=nx.random_regular_graph(3,12)

SatG21=nx.random_regular_graph(3,12)
SatG22=nx.random_regular_graph(3,12)

SatG31=nx.random_regular_graph(3,12)
SatG32=nx.random_regular_graph(3,12)

#接入卫星，2个子网，每个子网有三个
InSatG11=nx.random_regular_graph(3,30)
InSatG12=nx.random_regular_graph(3,40)

InSatG21=nx.random_regular_graph(3,30)
InSatG22=nx.random_regular_graph(3,40)

InSatG31=nx.random_regular_graph(3,30)
InSatG32=nx.random_regular_graph(3,40)

#地面子网，两个网络，第一个网络有70个结点，第二个网络有90个结点
LandG11=nx.random_regular_graph(3,100)
LandG12=nx.random_regular_graph(3,100)

LandG21=nx.random_regular_graph(3,100)
LandG22=nx.random_regular_graph(3,100)

LandG31=nx.random_regular_graph(3,100)
LandG32=nx.random_regular_graph(3,100)



tempSatG1=nx.random_regular_graph(3,12)
tempSatG2=nx.random_regular_graph(3,12)

#接入卫星，2个子网，每个子网有三个
tempInSatG1=nx.random_regular_graph(3,30)
tempInSatG2=nx.random_regular_graph(3,40)


#地面子网，两个网络，第一个网络有70个结点，第二个网络有90个结点
tempLandG1=nx.random_regular_graph(3 ,100)
tempLandG2=nx.random_regular_graph(3,100)


#图初始化
for item in range(0,SatG11.number_of_nodes()):
    SatG11.node[item]['category']=1
    SatG21.node[item]['category']=1
    SatG31.node[item]['category']=1
for item in range(0,SatG12.number_of_nodes()):
    SatG12.node[item]['category']=1
    SatG22.node[item]['category']=1
    SatG32.node[item]['category']=1
for item in range(0,InSatG11.number_of_nodes()):
    InSatG11.node[item]['category']=1
    InSatG21.node[item]['category']=1
    InSatG31.node[item]['category']=1
for item in range(0,InSatG12.number_of_nodes()):
    InSatG12.node[item]['category']=1
    InSatG22.node[item]['category']=1
    InSatG32.node[item]['category']=1
for item in range(0,LandG11.number_of_nodes()):
    LandG11.node[item]['category']=1
    LandG21.node[item]['category']=1
    LandG31.node[item]['category']=1
for item in range(0,LandG12.number_of_nodes()):
    LandG12.node[item]['category'] = 1
    LandG22.node[item]['category'] = 1
    LandG32.node[item]['category'] = 1


for item in range(0,tempSatG1.number_of_nodes()):
    tempSatG1.node[item]['category']=1
for item in range(0,tempSatG2.number_of_nodes()):
    tempSatG2.node[item]['category']=1
for item in range(0,tempInSatG1.number_of_nodes()):
    tempInSatG1.node[item]['category']=1
for item in range(0,tempInSatG2.number_of_nodes()):
    tempInSatG2.node[item]['category']=1
for item in range(0,tempLandG1.number_of_nodes()):
    tempLandG1.node[item]['category']=1
for item in range(0,tempLandG2.number_of_nodes()):
    tempLandG2.node[item]['category'] = 1

index1=1.0
index2=1.0
index3=1.0
index4=1.0
index5=1.0
index6=1.0


def index(request):
    return render(request, "index3.html")
def toindex2(request):
    return render(request,"index1.html")
def toindex3(request):
    return render(request,"index2.html")


def putSatG11InJson(request):
    for item in range(0,tempSatG1.number_of_nodes()):
        if SatG11.has_node(item):
            tempSatG1.node[item]['category'] = 3
        else:
            tempSatG1.node[item]['category'] = 1
    temp=json_graph.node_link_data(tempSatG1)
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
    return JsonResponse(retArr)

def putSatG21InJson(request):
    for item in range(0,tempSatG1.number_of_nodes()):
        if SatG21.has_node(item):
            tempSatG1.node[item]['category'] = 3
        else:
            tempSatG1.node[item]['category'] = 1
    temp=json_graph.node_link_data(tempSatG1)
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
    return JsonResponse(retArr)

def putSatG31InJson(request):
    for item in range(0,tempSatG1.number_of_nodes()):
        if SatG31.has_node(item):
            tempSatG1.node[item]['category'] = 3
        else:
            tempSatG1.node[item]['category'] = 1
    temp=json_graph.node_link_data(tempSatG1)
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
    return JsonResponse(retArr)


def putSatG12InJson(request):
    for item in range(0,tempSatG2.number_of_nodes()):
        if SatG12.has_node(item):
            tempSatG2.node[item]['category'] = 3
        else:
            tempSatG2.node[item]['category'] = 1
    temp=json_graph.node_link_data(tempSatG2)
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
    return JsonResponse(retArr)

def putSatG22InJson(request):
    for item in range(0,tempSatG2.number_of_nodes()):
        if SatG22.has_node(item):
            tempSatG2.node[item]['category'] = 3
        else:
            tempSatG2.node[item]['category'] = 1
    temp=json_graph.node_link_data(tempSatG2)
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
    return JsonResponse(retArr)

def putSatG32InJson(request):
    for item in range(0,tempSatG2.number_of_nodes()):
        if SatG32.has_node(item):
            tempSatG2.node[item]['category'] = 3
        else:
            tempSatG2.node[item]['category'] = 1
    temp=json_graph.node_link_data(tempSatG2)
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
    return JsonResponse(retArr)

def putInSatG11InJson(request):
    for item in range(0,tempInSatG1.number_of_nodes()):
        if InSatG11.has_node(item):
            tempInSatG1.node[item]['category'] = 3
        else:
            tempInSatG1.node[item]['category'] = 1
    temp=json_graph.node_link_data(tempInSatG1)
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
    return JsonResponse(retArr)

def putInSatG21InJson(request):
    for item in range(0,tempInSatG1.number_of_nodes()):
        if InSatG21.has_node(item):
            tempInSatG1.node[item]['category'] = 3
        else:
            tempInSatG1.node[item]['category'] = 1
    temp=json_graph.node_link_data(tempInSatG1)
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
    return JsonResponse(retArr)

def putInSatG31InJson(request):
    for item in range(0,tempInSatG1.number_of_nodes()):
        if InSatG31.has_node(item):
            tempInSatG1.node[item]['category'] = 3
        else:
            tempInSatG1.node[item]['category'] = 1
    temp=json_graph.node_link_data(tempInSatG1)
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
    return JsonResponse(retArr)

def putInSatG12InJson(request):
    for item in range(0,tempInSatG2.number_of_nodes()):
        if InSatG12.has_node(item):
            tempInSatG2.node[item]['category'] = 3
        else:
            tempInSatG2.node[item]['category'] = 1
    temp=json_graph.node_link_data(tempInSatG2)
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
    return JsonResponse(retArr)

def putInSatG22InJson(request):
    for item in range(0,tempInSatG2.number_of_nodes()):
        if InSatG22.has_node(item):
            tempInSatG2.node[item]['category'] = 3
        else:
            tempInSatG2.node[item]['category'] = 1
    temp=json_graph.node_link_data(tempInSatG2)
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
    return JsonResponse(retArr)

def putInSatG32InJson(request):
    for item in range(0,tempInSatG2.number_of_nodes()):
        if InSatG32.has_node(item):
            tempInSatG2.node[item]['category'] = 3
        else:
            tempInSatG2.node[item]['category'] = 1
    temp=json_graph.node_link_data(tempInSatG2)
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
    return JsonResponse(retArr)

def putLandG11InJson(request):
    for item in range(0,tempLandG1.number_of_nodes()):
        if LandG11.has_node(item):
            tempLandG1.node[item]['category'] = 3
        else:
            tempLandG1.node[item]['category'] = 1

    temp=json_graph.node_link_data(tempLandG1)
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
    return JsonResponse(retArr)

def putLandG21InJson(request):
    for item in range(0,tempLandG1.number_of_nodes()):
        if LandG21.has_node(item):
            tempLandG1.node[item]['category'] = 3
        else:
            tempLandG1.node[item]['category'] = 1

    temp=json_graph.node_link_data(tempLandG1)
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
    return JsonResponse(retArr)

def putLandG31InJson(request):
    for item in range(0,tempLandG1.number_of_nodes()):
        if LandG31.has_node(item):
            tempLandG1.node[item]['category'] = 3
        else:
            tempLandG1.node[item]['category'] = 1

    temp=json_graph.node_link_data(tempLandG1)
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
    return JsonResponse(retArr)

def putLandG12InJson(request):
    for item in range(0,tempLandG2.number_of_nodes()):
        if LandG12.has_node(item):
            tempLandG2.node[item]['category'] = 1
        else:
            tempLandG2.node[item]['category'] = 3
    temp=json_graph.node_link_data(tempLandG2)
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
    return JsonResponse(retArr)

def putLandG22InJson(request):
    for item in range(0,tempLandG2.number_of_nodes()):
        if LandG22.has_node(item):
            tempLandG2.node[item]['category'] = 1
        else:
            tempLandG2.node[item]['category'] = 3
    temp=json_graph.node_link_data(tempLandG2)
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
    return JsonResponse(retArr)

def putLandG32InJson(request):
    for item in range(0,tempLandG2.number_of_nodes()):
        if LandG32.has_node(item):
            tempLandG2.node[item]['category'] = 1
        else:
            tempLandG2.node[item]['category'] = 3
    temp=json_graph.node_link_data(tempLandG2)
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
    return JsonResponse(retArr)




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





#下面设计攻击
#本页面为第一种攻击模式：随机攻击

def tempAtt11():
    temp1=tempSatG1.number_of_nodes()
    for count1 in range(0,SatG11.number_of_nodes()):
        if SatG11.has_node(count1):
            SatG11.remove_node(count1)
        global index1
        index1=usable(SatG11,temp1)
        time.sleep(30)

def tempAtt12():
    temp2=tempSatG2.number_of_nodes()
    for count2 in range(0,SatG12.number_of_nodes()):
        if SatG12.has_node(count2):
            SatG12.remove_node(count2)
        global index2
        index2=usable(SatG12,temp2)
        time.sleep(31)

def tempAtt13():
    temp3=tempInSatG1.number_of_nodes()
    for count3 in range(0,InSatG11.number_of_nodes()):
        if InSatG11.has_node(count3):
            InSatG11.remove_node(count3)
        global index3
        index3=usable(InSatG11,temp3)
        time.sleep(11)

def tempAtt14():
    temp4=tempInSatG2.number_of_nodes()
    for count4 in range(0,InSatG12.number_of_nodes()):
        if InSatG12.has_node(count4):
            InSatG12.remove_node(count4)
        global index4
        index4=usable(InSatG12,temp4)
        time.sleep(10)

def tempAtt15():
    temp5=tempLandG1.number_of_nodes()
    for count5 in range(0,LandG11.number_of_nodes()):
        if LandG11.has_node(count5):
            LandG11.remove_node(count5)
        global index5
        index5=usable(LandG11,temp5)
        time.sleep(3)

def tempAtt16():
    temp6=tempLandG2.number_of_nodes()
    for count6 in range(0,LandG12.number_of_nodes()):
        if LandG12.has_node(count6):
            LandG12.remove_node(count6)
        global index6
        index6=usable(LandG12,temp6)
        time.sleep(2)

def att11(request):
    thread.start_new_thread(tempAtt11,())
    return render(request,"index3.html")

def att12(request):
    thread.start_new_thread(tempAtt12,())
    return render(request,"index3.html")

def att13(request):
    thread.start_new_thread(tempAtt13,())
    return render(request,"index3.html")

def att14(request):
    thread.start_new_thread(tempAtt14,())
    return render(request,"index3.html")

def att15(request):
    thread.start_new_thread(tempAtt15,())
    return render(request,"index3.html")

def att16(request):
    thread.start_new_thread(tempAtt16,())
    return render(request,"index3.html")



def pushData(request):
    global index1
    global index2
    global index3
    global index4
    global index5
    global index6
    allData=(index1+index4-index1*index4)*(index2+index5-index2*index5)*(index3+index6-index3*index6)*1000
    print allData
    dict={'inData':allData}
    return JsonResponse(dict)


def refresh1(request):
    global tempSatG1, tempSatG2, tempInSatG1, tempInSatG2, tempLandG1, tempLandG2
    global SatG11,SatG12,SatG21,SatG22,SatG31,SatG32
    global InSatG11,InSatG12,InSatG21,InSatG22,InSatG31,InSatG32
    global LandG11,LandG12,LandG21,LandG22,LandG31,LandG32
    
    for item in range(0, tempSatG1.number_of_nodes()):
        tempSatG1.node[item]['category'] = 1
    for item in range(0, tempSatG2.number_of_nodes()):
        tempSatG2.node[item]['category'] = 1
    for item in range(0, tempInSatG1.number_of_nodes()):
        tempInSatG1.node[item]['category'] = 1
    for item in range(0, tempInSatG2.number_of_nodes()):
        tempInSatG2.node[item]['category'] = 1
    for item in range(0, tempLandG1.number_of_nodes()):
        tempLandG1.node[item]['category'] = 1
    for item in range(0, tempLandG2.number_of_nodes()):
        tempLandG2.node[item]['category'] = 1
    SatG11 = nx.random_regular_graph(3, 12)
    SatG12 = nx.random_regular_graph(3, 12)
    SatG21 = nx.random_regular_graph(3, 12)
    SatG22 = nx.random_regular_graph(3, 12)
    SatG31 = nx.random_regular_graph(3, 12)
    SatG32 = nx.random_regular_graph(3, 12)

    # 接入卫星，2个子网，每个子网有三个
    InSatG11 = nx.random_regular_graph(3, 30)
    InSatG12 = nx.random_regular_graph(3, 40)
    InSatG21 = nx.random_regular_graph(3, 30)
    InSatG22 = nx.random_regular_graph(3, 40)
    InSatG31 = nx.random_regular_graph(3, 30)
    InSatG32 = nx.random_regular_graph(3, 40)

    # 地面子网，两个网络，第一个网络有70个结点，第二个网络有90个结点
    LandG11 = nx.random_regular_graph(3, 100)
    LandG12 = nx.random_regular_graph(3, 100)
    LandG21 = nx.random_regular_graph(3, 100)
    LandG22 = nx.random_regular_graph(3, 100)
    LandG31 = nx.random_regular_graph(3, 100)
#图初始化
    for item in range(0,SatG11.number_of_nodes()):
        SatG11.node[item]['category']=1
        SatG21.node[item]['category']=1
        SatG31.node[item]['category']=1
    for item in range(0,SatG12.number_of_nodes()):
        SatG12.node[item]['category']=1
        SatG22.node[item]['category']=1
        SatG32.node[item]['category']=1
    for item in range(0,InSatG11.number_of_nodes()):
        InSatG11.node[item]['category']=1
        InSatG21.node[item]['category']=1
        InSatG31.node[item]['category']=1
    for item in range(0,InSatG12.number_of_nodes()):
        InSatG12.node[item]['category']=1
        InSatG22.node[item]['category']=1
        InSatG32.node[item]['category']=1
    for item in range(0,LandG11.number_of_nodes()):
        LandG11.node[item]['category']=1
        LandG21.node[item]['category']=1
        LandG31.node[item]['category']=1
    for item in range(0,LandG12.number_of_nodes()):
        LandG12.node[item]['category'] = 1
        LandG22.node[item]['category'] = 1
        LandG32.node[item]['category'] = 1
    return render(request,"index1.html")

def refresh2(request):
    global tempSatG1, tempSatG2, tempInSatG1, tempInSatG2, tempLandG1, tempLandG2
    global SatG11,SatG12,SatG21,SatG22,SatG31,SatG32
    global InSatG11,InSatG12,InSatG21,InSatG22,InSatG31,InSatG32
    global LandG11,LandG12,LandG21,LandG22,LandG31,LandG32
    
    for item in range(0, tempSatG1.number_of_nodes()):
        tempSatG1.node[item]['category'] = 1
    for item in range(0, tempSatG2.number_of_nodes()):
        tempSatG2.node[item]['category'] = 1
    for item in range(0, tempInSatG1.number_of_nodes()):
        tempInSatG1.node[item]['category'] = 1
    for item in range(0, tempInSatG2.number_of_nodes()):
        tempInSatG2.node[item]['category'] = 1
    for item in range(0, tempLandG1.number_of_nodes()):
        tempLandG1.node[item]['category'] = 1
    for item in range(0, tempLandG2.number_of_nodes()):
        tempLandG2.node[item]['category'] = 1
    SatG11 = nx.random_regular_graph(3, 12)
    SatG12 = nx.random_regular_graph(3, 12)
    SatG21 = nx.random_regular_graph(3, 12)
    SatG22 = nx.random_regular_graph(3, 12)
    SatG31 = nx.random_regular_graph(3, 12)
    SatG32 = nx.random_regular_graph(3, 12)

    # 接入卫星，2个子网，每个子网有三个
    InSatG11 = nx.random_regular_graph(3, 30)
    InSatG12 = nx.random_regular_graph(3, 40)
    InSatG21 = nx.random_regular_graph(3, 30)
    InSatG22 = nx.random_regular_graph(3, 40)
    InSatG31 = nx.random_regular_graph(3, 30)
    InSatG32 = nx.random_regular_graph(3, 40)

    # 地面子网，两个网络，第一个网络有70个结点，第二个网络有90个结点
    LandG11 = nx.random_regular_graph(3, 100)
    LandG12 = nx.random_regular_graph(3, 100)
    LandG21 = nx.random_regular_graph(3, 100)
    LandG22 = nx.random_regular_graph(3, 100)
    LandG31 = nx.random_regular_graph(3, 100)
#图初始化
    for item in range(0,SatG11.number_of_nodes()):
        SatG11.node[item]['category']=1
        SatG21.node[item]['category']=1
        SatG31.node[item]['category']=1
    for item in range(0,SatG12.number_of_nodes()):
        SatG12.node[item]['category']=1
        SatG22.node[item]['category']=1
        SatG32.node[item]['category']=1
    for item in range(0,InSatG11.number_of_nodes()):
        InSatG11.node[item]['category']=1
        InSatG21.node[item]['category']=1
        InSatG31.node[item]['category']=1
    for item in range(0,InSatG12.number_of_nodes()):
        InSatG12.node[item]['category']=1
        InSatG22.node[item]['category']=1
        InSatG32.node[item]['category']=1
    for item in range(0,LandG11.number_of_nodes()):
        LandG11.node[item]['category']=1
        LandG21.node[item]['category']=1
        LandG31.node[item]['category']=1
    for item in range(0,LandG12.number_of_nodes()):
        LandG12.node[item]['category'] = 1
        LandG22.node[item]['category'] = 1
        LandG32.node[item]['category'] = 1
    return render(request,"index2.html")

def refresh3(request):
    global tempSatG1, tempSatG2, tempInSatG1, tempInSatG2, tempLandG1, tempLandG2
    global SatG11,SatG12,SatG21,SatG22,SatG31,SatG32
    global InSatG11,InSatG12,InSatG21,InSatG22,InSatG31,InSatG32
    global LandG11,LandG12,LandG21,LandG22,LandG31,LandG32
    
    for item in range(0, tempSatG1.number_of_nodes()):
        tempSatG1.node[item]['category'] = 1
    for item in range(0, tempSatG2.number_of_nodes()):
        tempSatG2.node[item]['category'] = 1
    for item in range(0, tempInSatG1.number_of_nodes()):
        tempInSatG1.node[item]['category'] = 1
    for item in range(0, tempInSatG2.number_of_nodes()):
        tempInSatG2.node[item]['category'] = 1
    for item in range(0, tempLandG1.number_of_nodes()):
        tempLandG1.node[item]['category'] = 1
    for item in range(0, tempLandG2.number_of_nodes()):
        tempLandG2.node[item]['category'] = 1
    SatG11 = nx.random_regular_graph(3, 12)
    SatG12 = nx.random_regular_graph(3, 12)
    SatG21 = nx.random_regular_graph(3, 12)
    SatG22 = nx.random_regular_graph(3, 12)
    SatG31 = nx.random_regular_graph(3, 12)
    SatG32 = nx.random_regular_graph(3, 12)

    # 接入卫星，2个子网，每个子网有三个
    InSatG11 = nx.random_regular_graph(3, 30)
    InSatG12 = nx.random_regular_graph(3, 40)
    InSatG21 = nx.random_regular_graph(3, 30)
    InSatG22 = nx.random_regular_graph(3, 40)
    InSatG31 = nx.random_regular_graph(3, 30)
    InSatG32 = nx.random_regular_graph(3, 40)

    # 地面子网，两个网络，第一个网络有70个结点，第二个网络有90个结点
    LandG11 = nx.random_regular_graph(3, 100)
    LandG12 = nx.random_regular_graph(3, 100)
    LandG21 = nx.random_regular_graph(3, 100)
    LandG22 = nx.random_regular_graph(3, 100)
    LandG31 = nx.random_regular_graph(3, 100)
#图初始化
    for item in range(0,SatG11.number_of_nodes()):
        SatG11.node[item]['category']=1
        SatG21.node[item]['category']=1
        SatG31.node[item]['category']=1
    for item in range(0,SatG12.number_of_nodes()):
        SatG12.node[item]['category']=1
        SatG22.node[item]['category']=1
        SatG32.node[item]['category']=1
    for item in range(0,InSatG11.number_of_nodes()):
        InSatG11.node[item]['category']=1
        InSatG21.node[item]['category']=1
        InSatG31.node[item]['category']=1
    for item in range(0,InSatG12.number_of_nodes()):
        InSatG12.node[item]['category']=1
        InSatG22.node[item]['category']=1
        InSatG32.node[item]['category']=1
    for item in range(0,LandG11.number_of_nodes()):
        LandG11.node[item]['category']=1
        LandG21.node[item]['category']=1
        LandG31.node[item]['category']=1
    for item in range(0,LandG12.number_of_nodes()):
        LandG12.node[item]['category'] = 1
        LandG22.node[item]['category'] = 1
        LandG32.node[item]['category'] = 1
    return render(request,"index3.html")


def tempAtt21():
    temp1=tempSatG1.number_of_nodes()
    score = nx.degree(tempSatG1)
    score = sorted(score, key=lambda score: score[1], reverse=True)
    output = []
    for node in score:
        output.append(node[0])
    for item in output:
        if SatG21.has_node(item):
            SatG21.remove_node(item)
        global index1
        index1=usable(SatG21,temp1)
        time.sleep(30)

def tempAtt22():
    temp2=tempSatG2.number_of_nodes()
    score = nx.degree(tempSatG2)
    score = sorted(score, key=lambda score: score[1], reverse=True)
    output = []
    for node in score:
        output.append(node[0])
    for item in output:
        if SatG22.has_node(item):
            SatG22.remove_node(item)
        global index2
        index2=usable(SatG22,temp2)
        time.sleep(31)

def tempAtt23():
    temp3=tempInSatG1.number_of_nodes()
    score = nx.degree(tempInSatG1)
    score = sorted(score, key=lambda score: score[1], reverse=True)
    output = []
    for node in score:
        output.append(node[0])
    for item in output:
        if InSatG21.has_node(item):
            InSatG21.remove_node(item)
        global index3
        index3=usable(InSatG21,temp3)
        time.sleep(11)

def tempAtt24():
    temp4=tempInSatG2.number_of_nodes()
    score = nx.degree(tempInSatG2)
    score = sorted(score, key=lambda score: score[1], reverse=True)
    output = []
    for node in score:
        output.append(node[0])
    for item in output:
        if InSatG22.has_node(item):
            InSatG22.remove_node(item)
        global index4
        index4=usable(InSatG22,temp4)
        time.sleep(10)

def tempAtt25():
    temp5=tempLandG1.number_of_nodes()
    score = nx.degree(tempLandG1)
    score = sorted(score, key=lambda score: score[1], reverse=True)
    output = []
    for node in score:
        output.append(node[0])
    for item in output:
        if LandG21.has_node(item):
            LandG21.remove_node(item)
        global index5
        index5=usable(LandG21,temp5)
        time.sleep(3)

def tempAtt26():
    temp6=tempLandG2.number_of_nodes()
    score = nx.degree(tempLandG1)
    score = sorted(score, key=lambda score: score[1], reverse=True)
    output = []
    for node in score:
        output.append(node[0])
    for item in output:
        if LandG22.has_node(item):
            LandG22.remove_node(item)
        global index6
        index6=usable(LandG22,temp6)
        time.sleep(3)

def att21(request):
    thread.start_new_thread(tempAtt21,())
    return render(request,"index1.html")

def att22(request):
    thread.start_new_thread(tempAtt22,())
    return render(request,"index1.html")

def att23(request):
    thread.start_new_thread(tempAtt23,())
    return render(request,"index1.html")

def att24(request):
    thread.start_new_thread(tempAtt24,())
    return render(request,"index1.html")

def att25(request):
    thread.start_new_thread(tempAtt25,())
    return render(request,"index1.html")

def att26(request):
    thread.start_new_thread(tempAtt26,())
    return render(request,"index1.html")




def tempAtt31():
    temp1=tempSatG1.number_of_nodes()
    score = nx.betweenness_centrality(SatG31)
    score = sorted(score.items(), key=lambda item: item[1], reverse=True)
    output = []
    for node in score:
        output.append(node[0])
    for item in output:
        if SatG31.has_node(item):
            SatG31.remove_node(item)
        global index1
        index1=usable(SatG31,temp1)
        time.sleep(30)

def tempAtt32():
    temp2=tempSatG2.number_of_nodes()
    score = nx.betweenness_centrality(SatG32)
    score = sorted(score.items(), key=lambda item: item[1], reverse=True)
    output = []
    for node in score:
        output.append(node[0])
    for item in output:
        if SatG32.has_node(item):
            SatG32.remove_node(item)
        global index2
        index2=usable(SatG32,temp2)
        time.sleep(31)

def tempAtt33():
    temp3=tempInSatG1.number_of_nodes()
    score = nx.betweenness_centrality(InSatG31)
    score = sorted(score.items(), key=lambda item: item[1], reverse=True)
    output = []
    for node in score:
        output.append(node[0])
    for item in output:
        if InSatG31.has_node(item):
            InSatG31.remove_node(item)
        global index3
        index3=usable(InSatG31,temp3)
        time.sleep(11)

def tempAtt34():
    temp4=tempInSatG2.number_of_nodes()
    score = nx.betweenness_centrality(InSatG2)
    score = sorted(score.items(), key=lambda item: item[1], reverse=True)
    output = []
    for node in score:
        output.append(node[0])
    for item in output:
        if InSatG32.has_node(item):
            InSatG32.remove_node(item)
        global index4
        index4=usable(InSatG32,temp4)
        time.sleep(10)

def tempAtt35():
    temp5=tempLandG1.number_of_nodes()
    score = nx.betweenness_centrality(LandG31)
    score = sorted(score.items(), key=lambda item: item[1], reverse=True)
    output = []
    for node in score:
        output.append(node[0])
    for item in output:
        if LandG31.has_node(item):
            LandG31.remove_node(item)
        global index5
        index5=usable(LandG31,temp5)
        time.sleep(3)

def tempAtt36():
    temp6=tempLandG2.number_of_nodes()
    score = nx.betweenness_centrality(LandG32)
    score = sorted(score.items(), key=lambda item: item[1], reverse=True)
    output = []
    for node in score:
        output.append(node[0])
    for item in output:
        if LandG32.has_node(item):
            LandG32.remove_node(item)
        global index6
        index6=usable(LandG32,temp6)
        time.sleep(3)

def att31(request):
    thread.start_new_thread(tempAtt11,())
    return render(request,"index2.html")

def att32(request):
    thread.start_new_thread(tempAtt12,())
    return render(request,"index2.html")

def att33(request):
    thread.start_new_thread(tempAtt13,())
    return render(request,"index2.html")

def att34(request):
    thread.start_new_thread(tempAtt14,())
    return render(request,"index2.html")

def att35(request):
    thread.start_new_thread(tempAtt15,())
    return render(request,"index2.html")

def att36(request):
    thread.start_new_thread(tempAtt16,())
    return render(request,"index2.html")

def thread1():
    thread.start_new_thread(tempAtt11,())
    thread.start_new_thread(tempAtt12,())
    thread.start_new_thread(tempAtt13,())
    thread.start_new_thread(tempAtt14,())
    thread.start_new_thread(tempAtt15,())
    thread.start_new_thread(tempAtt16,())

def thread2():
    thread.start_new_thread(tempAtt21,())
    thread.start_new_thread(tempAtt22,())
    thread.start_new_thread(tempAtt23,())
    thread.start_new_thread(tempAtt24,())
    thread.start_new_thread(tempAtt25,())
    thread.start_new_thread(tempAtt26,())

def thread3():
    thread.start_new_thread(tempAtt31,())
    thread.start_new_thread(tempAtt32,())
    thread.start_new_thread(tempAtt33,())
    thread.start_new_thread(tempAtt34,())
    thread.start_new_thread(tempAtt35,())
    thread.start_new_thread(tempAtt36,())

def format1data(request):
    dict={'index':index1}
    return JsonResponse(dict)

def format2data(request):
    dict={'index':index2}
    return JsonResponse(dict)

def format3data(request):
    dict={'index':index3}
    return JsonResponse(dict)

def format4data(request):
    dict={'index':index4}
    return JsonResponse(dict)

def format5data(request):
    dict={'index':index5}
    return JsonResponse(dict)

def format6data(request):
    dict={'index':index6}
    return JsonResponse(dict)


def toCompare(request):
    return render(request,"line-simple.html")