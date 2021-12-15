# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 19:04:41 2021

@author: Jay
"""

print("---------------------------")
print("| Welcome to Apple Store! |")
print("---------------------------")
a = 0
b = 0
c = 0
d = 0
m = []
while True:
    print("\n1.設定頻果數量,價錢""\n2.進貨數量""\n3.賣出數量,應收多少錢""\n4.營業額統計""\n5.庫存""\n6.離開系統")
    i = int(input("選擇要使用的功能"))
    if i == 1:
        a = int(input("蘋果的數量"))
        b = int(input("蘋果的價錢"))
    elif i == 2:
        c = int(input("進貨的數量"))
        a = a + c
    elif i == 3:
        d = int(input("賣出的數量"))
        a = a - d
        print("應收",b*d,"元")
        m.append([d,b*d])
    elif i == 4:
        f = 0
        g = 0
        for e in m:
            f = f + e[0]
            g = g + e[1]
        print("有",len(m),"筆交易,總共賣了",f,"個,共收",g,"元")
    elif i == 5:
        print("\n庫存還有",a,"個")
    elif i == 6:
        print("離開系統")
        break