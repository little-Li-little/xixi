#coding=utf-8
from math import gcd  #最大公约数
class Rational():
    def __init__(self,n,d):   #创建对象时，自动调用的初始化方法
        y=gcd(n,d)
        self.__n = n//y       #  //表整除
        self.__d = d//y
    def number(self):
        return self.__n
    def demon(self):
        return self.__d
    def print_Rational(self):
        print(self.__n,"/",self.__d)
        # self.__n = n
        # self.__d = d
    def __add__(self, other):
        if not isinstance(other,Rational):
            print("The element must be Rational")
            return False
        return Rational(self.__n*other.__d+other.__n*self.__d,self.__d*other.__d)
    def __str__(self):
        return "({}/{})".format(self.__n,self.__d)
    def __mul__(self, other):
        # if not isinstance(other,Rational):
            # print("The element must be Rational")
            # return False
        return Rational(self.__n*other.__n,self.__d*other.__d)
    def __equal__(self,other):
        if not isinstance(other,Rational):
            print("The element must be Rational")
            return False
        return  Rational(self.__n*other.__d==self.__d*other.__n)


t1=Rational(1,5)
t2=Rational(1,4)
print(t1,t2)
t=t1+t2
print(t1+t2)
print(t1*t2)
t3=Rational(1,10)
print(t==t3)

