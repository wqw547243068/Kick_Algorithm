
# 参考：图和树的python实现：https://www.cnblogs.com/5poi/p/7271447.html

# 邻接表

## 邻接集表示法

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

##  邻接表
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

## 加权邻接列表
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

# 邻接矩阵
## 嵌套list实现邻接矩阵
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

## 含无穷大的矩阵
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