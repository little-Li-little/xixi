#coding=utf-8
"""
函数式编程练习
"""
#练习fliter函数：使用filter函数过滤小于三的数;用法：filter(函数，列表)
a=[1,2,3,4,5,6,7,8,9]
result = filter(lambda x:x>3,a)
for x in result:
    print(x,end=" ")

#练习map函数：使用map函数将以下的所有数都扩大十倍；用法：map（函数，列表）
a=[1,2,3,4,5,6,7,8,9]
result = map(lambda x:x*10,a)
# for x in result:
#     print(x,end=" ")
print(list(result))  #转化为列表

#练习reduce函数：使用reduce函数求以下的列表中的数值之和；用法：reduce（函数，列表）
from functools import reduce
a=[1,2,3,4,5,6,7,8,9]
result = reduce(lambda x,y:x+y,a)
print(result)
