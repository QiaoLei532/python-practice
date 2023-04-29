"""
需求：
3.8
放眼世界
3.9
晚餐嘉宾
3.10
尝试使用各个函数
"""
#3.8放眼世界
places = ['China', 'Janpa', 'USA', 'UK', 'Russia']
print(f'我要去这些地方旅游{places}')
# print(f'临时排序sorted{places.sorted()}') p3 已经放弃这个函数了
places.sort()
print(places)
places.reverse()
print(places)

#3.10 各个函数使用
places.pop() #删除 默认最后一个
print(places)
places.append('China')
print(places)
places.sort() #排序 默认字母顺序 help()查看函数说明
print(places)
places.reverse() #反向排序
print(places)
places.extend('mamama') #扩充，逐个字母
print(places)
