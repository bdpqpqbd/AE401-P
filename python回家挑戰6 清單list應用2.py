# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 20:33:31 2021

@author: Jay
"""

a = int(input("全班人數"))
nameandscore = []
highscore = 0
lowscore = 100
highname = ""
lowname = ""
print("輸入",a,"個人的名子和分數")
for i in range(0,a):
    name = str(input("名子:"))
    nameandscore.append(name)
for i in range(1,a*2,2):
    score = int(input("成績:"))
    nameandscore.insert(i,score)
for i in range(0,a*2):
    print(nameandscore[i])
for i in range(0,a*2,2):
    if nameandscore[i+1] > highscore:
        highscore = nameandscore[i+1]
        highname = nameandscore[i]
    if nameandscore[i+1] < lowscore:
        lowscore = nameandscore[i+1]
        lowname = nameandscore[i]
print("最高分:",highname,highscore)
print("最低分:",lowname,lowscore)