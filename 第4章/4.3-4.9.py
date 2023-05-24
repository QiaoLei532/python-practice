"""
需求
4.3 1-20打印
4.4 一百万
4.5 计算1~100W
4.6 奇数
4.7 3的倍数
4.8 立方
4.9 立方解析
"""
# 4.3 1-20打印
for i in range(1, 21):
    print(i,end=',')

# 4.4 100W
list1 = list(range(1, 1000001))
print(list1)

# 4.5 sum 1~100W
print(f'list1列表最小值为{min(list1)},最大值为{max(list1)},和为{sum(list1)}')

# 4.6 奇数
for i in range(1, 21, 2):
    print(i, end=',')
print()

# 4.7 3的倍数
squre = []
for i in range(1, 11):
    squre.append(i * 3)
for j in squre:
    print(j, end=',')
print()

# 4.8 立方
q = []
for i in range(1, 11):
    i = i**3
    q.append(i)
for j in q:
    print(j, end=',')
print()

# 4.9 立方解析
list2 = list(i**3 for i in range(1, 11))
print(list2)