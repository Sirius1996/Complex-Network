# -*- coding: utf-8 -*-  
import networkx as nx
import matplotlib.pyplot as plt
from pylab import mpl                           #解决中文显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei']    #指定默认字体
import numpy as np

#check connectivity
#定义一个函数，去检查图的连通性
def reachable_nodes(G,start):
    seen=set()                                  #一个空集
    stack=[start]                               #一个空栈，将start放入
    while stack:
        node=stack.pop()
        if node not in seen:
            seen.add(node)
            stack.extend(G.neighbors(node))     #将这个结点都全部邻居入栈
    return seen                                 #seen最后即存放所有邻居结点

def is_connected(G):
    for start in G:
        reachable=reachable_nodes(G,start)
    return len(reachable)==len(G)

#检查图的强连通性（对于有向图）：
def directed_reachable_nodes(G,start):
    seen=set()
    stack=[start]
    while(stack):
        node=stack.pop()
        if node not in seen:
            seen.add(node)
            stack.extend(G.successors(node))
    return seen

def directed_is_connected(G):
    for start in G:
        reachable=directed_reachable_nodes(G,start)
        if len(reachable)<len(G):
            return False
    return True

#check Probability of connectivity
#检查连通概率
def connected_prob(n,p,iters):
    num=0.0
    for i in range(iters):
        random_graph = nx.erdos_renyi_graph(n,p)
        if is_connected(random_graph):
            num+=1
    return float(num/iters)





#构造一个有20个结点，每个节点度为3度规则分布网络
RG=nx.random_regular_graph(3,20)
pos = nx.spectral_layout(RG)
# nx.draw(RG, pos, with_labels = False, node_size = 30)
# plt.show()


ER=nx.erdos_renyi_graph(20,0.2)
pos=nx.shell_layout(ER)
# nx.draw(ER,pos,with_labels=True)
# plt.show()

#test:判断两个图分别是否连通
print is_connected(RG)
print is_connected(ER)

G=nx.Graph()
G.add_node(1)
G.add_node(2)
print is_connected(G)

n=10
print connected_prob(n,0.2,iters=1000)
pstar = np.log(n) / n
print pstar

ps = np.logspace(-1.3, 0, 11)
print ps

#每个输入概率，检验1000次，打印
ys = [connected_prob(n, p, 1000) for p in ps]
for p, y in zip(ps, ys):
    print(p, y)

plt.figure()
plt.plot(ps,ys)
plt.show()

