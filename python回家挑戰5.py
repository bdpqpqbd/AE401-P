# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 21:42:10 2021

@author: Jay
"""

a = int(input("全班人數"))
b = a
c = 0
d = 0
score = []
highest = 0
lowest = 100
print("輸入",a,"個人的分數")
while a > 0:
    a = a-1
    d = int(input())
    score.append(d)
    c = c+d
for e in score:
    if e > highest:
        highest = e
for e in score:
    if e < lowest:
        lowest = e
print("平均值:",c/b)
print("最高分:",highest)
print("最低分:",lowest)
