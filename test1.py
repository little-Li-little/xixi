#coding=utf-8
"""
定义函数，实现"幸运七"游戏
函数lucky(a,b)
a表示你的初始值
b表示你准备见好就收的钱数
打印出次数，游戏过程中最高钱数
"""
import random
def my_roll():#模拟掷骰子，掷两次
    points=[]
    for i in range(2):
        point=random.randint(1,6)
        points.append(point)
    return points
def gameone(points):#两次的和是否为7
    if sum(points)==7:
        return True
    else:
        return False
def lucky(a,b):
    money=a
    times=0
    maxmoney=money
    while 0<money<b:
        times+=1
        points=my_roll()
        result=gameone(points)
        if result:
            money+=4
        else:
            money-=1
        if money>maxmoney:
            maxmoney=money
    print("钱数是：",money,"次数是",times)
    print("最大值是",maxmoney)
lucky(100,120)