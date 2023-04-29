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
print('找到一个大桌子，加人！')
names.insert(0, 'Wangshuo')
names.insert(len(names)//2, 'Tina')
names.append('Qiaol')
for i in names:
    print(i+'，你好，我邀请你共进晚餐！')
#3.7缩减名单
print('桌子到不了了，只能邀请2个人！')
while len(names) > 2:
    name = names.pop()
    print(f'抱歉{name},无法邀请你了，下次吧！')
for i in names:
    print(i+'，你好，我邀请你共进晚餐！')
#del删除 新版本可以使用names.clear() 实现
while len(names) > 0:
    del names[len(names)-1]
print(names)