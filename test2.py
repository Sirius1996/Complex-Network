# -*- coding: utf-8 -*-
import networkx as nx
import threading

G=nx.random_regular_graph(3,200)

# 网络性能指标
# 接下来进行对每一个子网对攻击，并返回指标
def reachable_nodes(G, start):
    seen = set()  # 一个空集
    stack = [start]  # 一个空栈，将start放入
    while stack:
        node = stack.pop()
        if node not in seen:
            seen.add(node)
            stack.extend(G.neighbors(node))  # 将这个结点的全部邻居入栈
    return len(seen)  # seen最后即存放所有邻居结点


def is_connected(G):
    for start in G:
        reachable = reachable_nodes(G, start)
    return len(reachable) == len(G)


def usable(G, nodesNum):
    flag = 0
    tempCount = 1
    sumNum = 0.0
    for i in G:
        if flag == 0:
            sumNum = sumNum + reachable_nodes(G, i) * (reachable_nodes(G, i) - 1)
            flag = 1
            tempCount = tempCount + 1
        elif flag == 1:
            if tempCount == reachable_nodes(G, i):
                flag = 0
                tempCount = 1
            else:
                tempCount = tempCount + 1
    return float(sumNum / (nodesNum * (nodesNum - 1)))