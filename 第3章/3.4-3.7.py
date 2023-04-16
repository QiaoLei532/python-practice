"""
需求：
3.4嘉宾名单
3.5修改嘉宾名单
3.6添加嘉宾
3.7缩减名单
步骤分析：
1、准备一个3个姓名的列表
2、遍历
"""
#3.4嘉宾名单
names = ['Li Lei', 'han meimei', 'xiao ming']
for i in names:
    print(i+'，你好，我邀请你共进晚餐！')
#3.5修改嘉宾名单
print(names.pop(1)+'临时有事无法参加')
names.append('xiao hong')
for i in names:
    print(i+'，你好，我邀请你共进晚餐！')
#3.6添加嘉宾
