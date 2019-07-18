
# 图的Python实现
- 参考：[图和树的python实现](https://www.cnblogs.com/5poi/p/7271447.html)

# 邻接表

## 邻接集表示法
```python
a, b, c, d, e, f, g, h = range(8)
N = [
 {b, c, d, e, f},        # a
 {c, e},                 # b
 {d},                    # c
 {e},                    # d
 {f},                    # e
 {c, g, h},              # f
 {f, h},                 # g
 {f, g}                  # h
]
```

##  邻接表
```python
a, b, c, d, e, f, g, h = range(8)
N = [
 [b, c, d, e, f],        # a
 [c, e],                 # b
 [d],                    # c
 [e],                    # d
 [f],                    # e
 [c, g, h],              # f
 [f, h],                 # g
 [f, g]                  # h
]
```
## 加权邻接列表
```python
a, b, c, d, e, f, g, h = range(8)
N = [
 {b:2, c:1, d:3, e:9, f:4},   # a
 {c:4, e:3},                  # b
 {d:8},                       # c
 {e:7},                       # d
 {f:5},                       # e
 {c:2, g:2, h:2},             # f
 {f:1, h:6},                  # g
 {f:9, g:8}                   # h
]
```
# 邻接矩阵
## 嵌套list实现邻接矩阵
```python
a, b, c, d, e, f, g, h = range(8)
# a b c d e f g h
N = [[0,1,1,1,1,1,0,0], # a
     [0,0,1,0,1,0,0,0], # b
     [0,0,0,1,0,0,0,0], # c
     [0,0,0,0,1,0,0,0], # d
     [0,0,0,0,0,1,0,0], # e
     [0,0,1,0,0,0,1,1], # f
     [0,0,0,0,0,1,0,1], # g
     [0,0,0,0,0,1,1,0]] # h
```
## 含无穷大的矩阵
```python
inf = float('inf')
a, b, c, d, e, f, g, h = range(8)
# a b c d e f g h
N = [[inf, 1 , 1 , 1 , 1 , 1 ,inf,inf], # a
     [inf,inf, 1 ,inf, 1 ,inf,inf,inf], # b
     [inf,inf,inf, 1 ,inf,inf,inf,inf], # c
     [inf,inf,inf,inf, 1 ,inf,inf,inf], # d
     [inf,inf,inf,inf,inf, 1 ,inf,inf], # e
     [inf,inf, 1 ,inf,inf,inf, 1 , 1 ], # f
     [inf,inf,inf,inf,inf, 1 ,inf, 1 ], # g
     [inf,inf,inf,inf,inf, 1 , 1 ,inf]] # h
```
## 图遍历
```python
'''a指向b，a指向d，依次类推'''
charts = {'a':['b','d'],'c':['e'],'d':['c','e']}
 
'''遍历图中的路径'''
def path(chart,x,y,pathd=[]):
    pathd = pathd + [x]
    if x == y:
        return pathd
    if not chart.has_key(x):
        return None
 
    for jd in chart[x]:
        if jd not in pathd:
            newjd =path(chart,jd,y,pathd)
            if newjd:
                return newjd
 
print(path(charts,'a','e'))
```

```python
# -*- encoding:utf-8 -*-
'''

 A --> B
 A --> C
 B --> C
 B --> D
 C --> D
 D --> C
 E --> F
 F --> C

'''
def find_path(graph, start, end, path=[]):
        '寻找一条路径'
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath:
                    return newpath
        return path

def find_all_paths(graph, start, end, path=[]):
        '查找所有的路径'
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def find_shortest_path(graph, start, end, path=[]):
        '查找最短路径'
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

#test

if __name__ == '__main__':
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
    print find_path(graph,'A','D')
    print find_all_paths(graph,'A','D')
    print find_shortest_path(graph,'A','D')
```


# 别的实现版本
- [图的实现](https://blog.csdn.net/Liangjun_Feng/article/details/77585298)

首先给出一个使用邻接矩阵建立的图类，输入参数为图的邻接矩阵，同时，还会有一个unconn参数用以设定无关联情况的特殊值，默认值为0

```python

inf = float('inf')  #定义一个无穷大的量表示无边情况


#采用邻接矩阵实现
class Graph:
    def __init__(self,mat,unconn = 0):   #初始化
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("Argument for 'Graph'.")
        self._mat = [mat[i][:] for i in range(vnum)]      #使用拷贝的数据
        self._unonn = unconn
        self._vnum = vnum

    def vertex_num(self):      #返回结点数目
        return self._vnum

    def _invalid(self,v):      #检验输入的结点是否合法
        return v > 0 or v >= self._vnum

    def add_adge(self,vi,vj,val=1):   #增加边
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or' + str(vj) + 'is not a valid vertex.')
        self._mat[vi][vj] = val

    def get_adge(self,vi,vj):   #得到边的信息
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or' + str(vj) + 'is not a valid vertex.')
        return self._mat[vi][vj]

    def out_edges(self,vi):    #得到vi出发的所有边
        if self._invalid(vi):
            raise GraphError(str(vi)+' is not a valid vertex.')
        return self._out_edges(self._mat[vi],self._unconn)

    @staticmethod
    def _out_edges(row,unconn): #辅助函数
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i,row[i]))
        return edges

    def __str__(self):          #输出的str方法
        return '[\n' + ',\n'.join(map(str,self._mat)) + '\n]' + '\nUnconnected: ' + str(self._unconn)
 ```   

## 邻接表

```python

#采用邻接表实现，需要重写一些方法，但功能相同
class GraphAL(Graph):      #继承于Graph
    def __init__(self,mat=[],unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) !=vnum:
                raise ValueError("Argument for 'Graph'.")
        self._mat = [Graph._out_edges(mat[i],unconn) for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn

    def add_edge(self,vi,vj,val = 1):
        if self._vnum == 0:
            raise GraphError('Cannot add edge to empty graph.')
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or' + str(vj) + ' is not valid vertex.')

        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj,val)
                return
            if row[i][0] > vj:
                break
            i += 1
        self._mat[vi].insert(i,(vj,val))

    def get_edge(self,vi,vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or' + str(vj) + ' is not valid vertex.')
        for i,val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    def out_edges(self,vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + ' is not valid vertex.')

        return self._mat[vi]
```

## 图遍历
图的遍历是图的操作算法中最基本也是最重要的方法，与树的遍历相似，这里也分为深度优先遍历和宽度优先遍历，通过深度优先遍历得到的顶点序列称为该图的深度优先序列(Depth-First Search,DFS序列），通过宽度优先遍历得到的顶点序列称为该图的宽度优先序列（Breadth-First Search,BFS序列） 
这里给出非递归的深度遍历算法，算法里采用了一个内部的表对象记录访问历史，对应每个顶点有一个表元素，当一个顶点被访问时，将该顶点下标对应的表元素设置为1，初始值全部为0

```python
import SStack             #在之前的栈章节里有源码
#图的深度优先遍历算法
def DFS_graph(graph,v0):
    vnum = graph.vertex_num()
    visited = [0]*vnum    #用于记录已访问结点
    visited[v0] = 1
    DFS_seq = [v0]        #记录遍历顺序
    st = SStack()
    st.push((0,graph.out_edges(v0)))   #入栈
    while not st.is_empty():
        i,edges = st.pop()
        if i < len(edges):
            v,e = edges[i]
            st.push((i+1,edges))       #下次访问
            if not visited[v]:
                DFS_seq.append(v)
                visited[v] = 1
                st.push((0,graph.out_edges(v)))
    return DFS_seq
```

## 最小生成树
图是实际中经常运用到的数据结构，这里列举出两个经典的问题，给出解决算法 

1.最小生成树解法 
- 假定G是一个网络，其中的边带有给定的权值，可以做出它的生成树，现将G的一棵生成树中各条边的权值之和称为该生成树的权。网络G可能存在许多棵不同的生成树，不同生成树的权值也有可能不同，其中权值最小的生成树称为G的最小生成树 

### kruscal

Kruskal算法是一种构造最小生成树的简单算法，其中的思想也比较简单 

算法思想： 
- （1）设G = （V，E）是一个网络，其中|V| = n。初始时取包含G中所有n个顶点但没有任何边的孤立点子图T= (V,{}),T里的每一个顶点自成一个连通分量 
- （2）将边集E中的边按权值递增的顺序排列，在构造中的每一步顺序地检查这个边序列，找到下一条（最短的）两端点位于T的两个不同连通分量的边e，把e加入T。这导致两个连通分量由于边e的连接而变成了一个连通分量 
- （3）每次操作使T减少一个连通分量，不断重复这个动作加入新边，直到T中所有顶点都包含在一个连通分量里为止，这个连通分量就是G的一棵最小生成树

```python
#Krudkal最小生成树算法
def Kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst,edges = [],[]
    for vi in range(vnum):  #所有边入表
        for v,w in graph.out_edges(vi):
            edges.append((w,vi,v))
    edges.sort()            #按权值排序
    for w,vi,vj in edges:
        if reps[vi] != reps[vj]:
            mst.append((vi,vj),w)
            if len(mst) == vnum - 1:
                break
            rep,orep = rep[vi],reps[vj]
            for i in range(vnum):  #合并连通分量
                if reps[i] == orep:
                    reps[i] = rep
    return mst
```

### prim
Prim算法基于最小生成树的一个重要性质，MST性质如下： 
- 设G=（V，E）是一个网络，U是V的一个任意真子集，e为G的一条边，一个端点在U里，另一个不在，而且e的权值与其他同情况的边相比最小，那么G必有一棵包括边e的最小生成树 

算法思想： 
- （1）从图G的顶点集V中任取一顶点放入集合U中，这时U = {v0},令边集合ET = {},显然T=（U，ET）是一棵树 
- （2）检查所有一个端点在集合U里而另一个端点在集合V-U的边，找出其中权最小的边，将不再U的顶点加入，并将e加入边集合ET 
- （3）重复步骤（2）直到U=V，这时子图T就是G的一棵最小生成树

```python
class PrioQueueError(ValueError):
    pass

#使用list实现基于堆的优先序列
（这是额外的内容，帮助Prim算法的实现）
class PrioQueue:
    def __init__(self,elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def enqueue(self,e):
        self._elems.append(None)
        self.siftup(e,len(self._elems)-1)

    def siftup(self,e,last):
        elems,i,j = self._elems,last,(last-1)//2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i,j, = j,(j-1)//2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in dequeue')
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e,0,len(elems))
        return e0

    def siftdown(self,e,begin,end):
        elems,i,j = self._elems,begin,begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i,j = j,2*j+1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end//2.-1,-1):
            self.siftdown(self._elems[i],i,end)          

#Prim最小生成树法
def Prim(graph):
    vnum = graph.vertex_num()
    mst = [None]*vnum
    cands = PrioQueue([(0,0,0)])
    count = 0
    while count < vnum and not cands.is_empty():
        w,u,v = cands.dequeue()
        if mst[v]:
            continue
        mst[v] = ((u,v),w)
        count += 1
        for vi,w in graph.out_edges(v):
            if not mst[vi]:
                cands.enqueue((w,v,vi))
    return mst
```

## 最短路径
最短路径问题可以分为两种：
- 单源最短路径问题，即从一个顶点出发到图中其余各顶点的最短路径问题；
- 所有顶点之间的最短路径问题 
这里由于篇幅原因只给出算法实现，具体的思路，读者可以根据代码自己解析，或查阅相关资料 
### dijsktra

```python
import PrioQueue

#Dijkstra算法
def dijkstra_shortest_paths(graph,v0):
    vnum = graph.vertex_num()
    assert 0 <= v0 <= vnum
    paths = [None]*vnum
    count = 0
    cands = PrioQueue([(0,v0,v0)])     #初始队列
    while count < vnum and not cands.is_empty():
        plen,u,vmin = cands.dequeue()  #取顶点
        if paths[vmin]:
            continue
        paths[vmin] = (u,plen)         #记录路径
        for v,w in graph.out_edges(vmin):
            if not paths[v]:
                cands.enqueue((plen + w,vmin,v))
        count += 1
    return paths
```

### Floyd

```python
def all_shortest_paths(graph):
    vnum = graph.vertex_num()
    a = [[graph.get_edge(i,j) for j in range(vnum)] for i in range(vnum)]
    nvertex = [[-1 if a[i][j] == inf else j for j in range(vnum)] for i in range(vnum)]

    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][k]
                    nevertex[i][j] = nevertex[i][k]
    return (a,nevertex)
```

