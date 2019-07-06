# -*- coding: utf-8 -*-
# 原文：https: // blog.csdn.net / mxz19901102 / article / details / 80071864
class queue(object):
    def __init__(self):
        self.queue = []

    # 一次入队一个
    def inqueue(self, item):
        self.queue.append(item)

    # 一次入队多个
    def many_in_queue(self, *args):
        self.queue.extend(args)

    # 出队
    def outqueue(self):
        if not self.queue == []:
            self.queue.pop(0)
        else:
            return None

    # 显示队列
    def show(self):
        for i in self.queue:
            print
            i

    # 队列的头部
    def head(self):
        if not self.queue == []:
            print
            self.queue[0]
        else:
            return None

    # 队列的尾部
    def tail(self):
        if not self.queue == []:
            print
            self.queue[-1]
        else:
            return None

    # 是否为空
    def isempty(self):
        return self.queue == []

    # 长度
    def length(self):
        print
        len(self.queue)

if __name__ == '__main__':
    q1 = queue()
    q1.inqueue(1)
    q1.show()
    print('----------1-----------')
    q1.many_in_queue(3, 4, 5)
    q1.show()
    print('----------1-----------')
    q1.outqueue()
    q1.show()
    print('----------1-----------')
    q1.head()
    print('----------1-----------')
    q1.tail()
    print('----------1-----------')
    q1.length()
    q1.isempty()