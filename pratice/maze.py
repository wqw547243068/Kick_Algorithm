
# 利用栈解决迷宫问题
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [lambda x, y: (x + 1, y),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y - 1),
        lambda x, y: (x, y + 1)]

def mpath(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while len(stack) > 0:
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:
            #到达终点
            for p in stack:
                print(p)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                #找到了下一个
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = -1  # 标记为已经走过，防止死循环
                break
        else:#四个方向都没找到
            maze[curNode[0]][curNode[1]] = -1  # 死路一条,下次别走了
            stack.pop() #回溯
    print("没有路")
    return False

mpath(1,1,8,8)

# 利用队列解决迷宫问题
from collections import  deque

mg = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [lambda x, y: (x + 1, y),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y - 1),
        lambda x, y: (x, y + 1)]

def print_p(path):
    curNode = path[-1]
    realpath = []
    print('迷宫路径为：')
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]
    realpath.append(curNode[0:2])
    realpath.reverse()
    print(realpath)

def mgpath(x1, y1, x2, y2):
    queue = deque()
    path = []
    queue.append((x1, y1, -1))
    while len(queue) > 0:
        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            #到达终点
            print_p(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if mg[nextNode[0]][nextNode[1]] == 0:  # 找到下一个方块
                queue.append((*nextNode, len(path) - 1))
                mg[nextNode[0]][nextNode[1]] = -1  # 标记为已经走过
    return False


mgpath(1,1,8,8)