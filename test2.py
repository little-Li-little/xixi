#coding=utf-8
r=1#控制行数
c=1#控制列数
for r in range(1,10):
    for c in range(1,r+1):
        print("%s*%s=%s"%(c,r,r*c),end="\t")
    r=1
    print("") #起到换行的作用

