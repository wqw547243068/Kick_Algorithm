# 巧用Python列表特性实现特定数据结构

## 栈实现

```python
stack = []
stack.push(x)
stack.pop()
stack[-1]
```


## 队列实现

```python
from collections import deque
queue = deque()
```

## 单向队列
```python
queue.append(x)
queue.popleft()
```

## 双向队列
```python
queue.append(x)
queue.popleft()
queue.appendleft(x)
queue.pop()
```


## 环形队列
```python
#初始
dqueue = []
rear = 0
front = 0
#添加一个数据
front = (front + 1 ) % MaxSize
#一个数据出队
rear = (rear + 1 ) % MaxSize
#空队条件
rear == front
#满队条件
(rear + 1 ) % MaxSize == front
```


## 链表实现
```python
class Node(object):
def __init__(self,item=None):
　　self.item = item
　　self.next = None

def main():
　　head = Node(1)
　　b = Node(2)
　　head.next = b
```
head -> b -> None
```python
#head为链表首部,有无数据都可以
#遍历链表
def traversal(head):
　　currNode = head
　　while currNode is not None:
　　　　print(currNode.item)
　　　　currNode = currNode.next
#链表的插入、删除
#插入
#p.next = currNode.next
#currNode.next = p
#删除
#currNode.next = p
#currNode.next = currNode.next.next
#del p
```


## 双向链表
```python
class Node(object):
def __init__(self,item=None):
　　self.item = itme
　　self.next = None
　　self.prev = None
#插入
#p.next = currNode.next
#currNode.next.prev = p
#p.prev = currNode
#currNode.next = p
#删除
#p = currNode.next
#currNode.next = p.next
#p.next.prev = currNode
#del p
```


## 链表分析 
- 链表和列表的效率分析
- 按元素查找时间复杂度都为O(n)
- 按下标查找链表时间复杂度为O(n),列表为O(1)
- 在某元素后插入数据链表时间复杂度为O(1),列表的时间复杂度为O(n)
- 删除某元素链表时间复杂度为O(n),列表时间复杂度为O(1)




## 散列表（Hash表）实现
- 它是一种线性存储的表结构
- 首先根据关键字k，进过某Hash函数，获得一个索引值
- 然后将该关键字存储到索引值所在的位置

这也是集合的存储原理

对于字典也是类似的

字典是对每一个key求索引值，索引值对应的位置存放相应的value

问题一：
- 索引值重复
   - 解决一：线性表每个位置采用链表存储，相同索引值得关键字，依次链接起来（拉链法
   - 解决二：通过哈希冲突函数得到新的地址（开放地址法）
