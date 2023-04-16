"""
需求：
删除人名中的空白
步骤分析：
1、准备一个变量
2、打印
3、去除左空白
4、去除右空白
5、全部去除
"""
name = '\t Li Lei\t\n'
print('姓名'+name+'。')
print('取消左空白'+name.lstrip()+'。')
print('取消右空白'+name.rstrip()+'。')
print('取消全部空白'+name.strip()+'。')

