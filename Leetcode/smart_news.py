# [2020-3-18] smartnews编程题目
# 找字符串的解码数目
'''
Your previous Markdown content is preserved below:

A message containing letters from A-Z is being encoded to numbers using the following mapping:

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

```
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
```

Example 2:

```
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```
'''

def find_num(s):
    """ find all numbers """
    if not s:
        return 1
    elif len(s) == 1:
        return 1
    else:
        prefix = int(s[:2])
        if prefix <= 26: # 2 char
            return find_num(s[2:]) + find_num(s[1:])
        else: # 1 char
            return find_num(s[1:])

if __name__ == "__main__":
    print('测试如下')
    a_list = ['12', '26', '62','226', '3145', '1212']
    for a in a_list:
        print('The num of {} is {}'.format(a, find_num(a)))





