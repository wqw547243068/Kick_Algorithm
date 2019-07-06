# -*- coding: utf-8 -*-
# 原文：https: // blog.csdn.net / mxz19901102 / article / details / 80071864
class Stack(object):

    # 限定Stack类的成员只有__items(类成员)
    __slots__ = ('__items')

    # 初始化栈为空列表
    def __init__(self):
        self.__items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.__items == []

    # 返回栈顶元素
    def peek(self):
        return self.__items[len(self.__items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.__items)

    # 把新的元素堆进栈里面（程序员喜欢把这个过程叫做压栈，入栈，进栈……）
    def push(self, item):
        self.__items.append(item)

    # 把栈顶元素丢出去（程序员喜欢把这个过程叫做出栈……）
    def pop(self):
        return self.__items.pop()

if __name__ == '__main__':
    # 初始化一个栈对象
    my_stack = Stack()
    # 把'h'丢进栈里
    my_stack.push('h')
    # 把'a'丢进栈里
    my_stack.push('a')
    # 看一下栈的大小（有几个元素）
    print(my_stack.size())
    # 打印栈顶元素
    print(my_stack.peek())
    # 把栈顶元素丢出去，并打印出来
    print(my_stack.pop())
    # 再看一下栈顶元素是谁
    print(my_stack.peek())
    # 这个时候栈的大小是多少？
    print(my_stack.size())
    # 再丢一个栈顶元素
    print(my_stack.pop())
    # 看一下栈的大小
    print(my_stack.size)
    # 栈是不是空了？
    print(my_stack.is_empty())