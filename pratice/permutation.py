
class Solution(object):
    """解题类"""

    def __init__(self):
        pass
    
    def swap(self, arr, i, j):
        """ 交换数组两个数值 """
        if not arr:
            return 
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        return arr
    
    def permutation(self, arr, s, e):
        """ 打印全排列 """
        if not arr:
            print('arr为空，退出')
            return
        # 排列遍历完毕
        if s == e:
            print('\t'.join(arr))
            return
        # 削减规模，递归
        for i in range(s, e):
            self.swap(arr, s, i) # 替换已有元素
            self.permutation(arr, s+1, e)
            self.swap(arr, s, i) # 换回去
        pass

if __name__ == '__main__':
    arr = ['a', 'b', 'f', 'c', 'g', 'd']
    arr = ['a', 'b', 'f']
    test = Solution()
    test.permutation(arr, 0, len(arr))