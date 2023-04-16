"""
需求：问候语
步骤分析：
1、准备姓名列表
2、遍历优化输出
"""
names = ['Lily', 'Han Meimei', 'Xiao Ming', 'Xiao Hong']
for i in names:
    print(f'{i.title()},nice to meet you!')
j = 0
while j < len(names):
    print(f'{names[j]},nice to meet you!')
    j += 1