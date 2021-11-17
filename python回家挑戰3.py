# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 23:17:55 2021

@author: Jay
"""

import random
num = (random.randint(1, 20))
i = 0
num1 = 0
while i < 5 and num != num1:
    num1=int(input("猜一個數"))
    i = i+1
    if num1 > num:
        print("太大")
    elif num1 < num:
        print("太小")
    else:
        print("猜對了")
print("猜了",i,"次")
print("答案是",num)
