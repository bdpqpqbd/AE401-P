# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 19:02:45 2021

@author: Jay
"""

print("* * * * * * * * * * * * * * * *")
print("* Welcome to the dictionary!  *")
print("* * * * * * * * * * * * * * * *")
a = {
     }
b = 0
c = 0
f = 0
j = 0
l = 0
while True:
    print("\n1.新增單字\n2.查看單字\n3.英翻中\n4.中翻英\n5.測驗\n6.離開")
    b = int(input("選擇要使用的功能"))
    if b == 1:
        e = True
        while e:
            c = input("請輸入要新增的英文單字(退出請按0):")
            if c == "0":
                e = False
            else:
                d = input("請輸入中文意思:")
                a[c] = d
    elif b == 2:
        for i in a:
            print("\n英:",i,"中:",a[i])
    elif b == 3:
        f = input("請輸入想知道意思的英文單字:")
        if f not in a:
            print("\n字典裡沒有這個字")
        else:
            print("\n",a[f])
    elif b == 4:
        h = 0
        g = input("請輸入想知道意思的中文單字:")
        for i in a:
            if a[i] == g:
                print(i)
                h = 1
        if h == 0:
                print("\n字典裡沒有這個字")
    elif b == 5:
            k = 0
            for i in a:
                print("英文:",i)
                j = input("中文:")
                if j == a[i]:
                    print("答對了")
                    k = k + 1
                else:
                    print("答錯了")
            print("共",len(a),"題,答對",k,"題,答錯",len(a)-k,"題")
    elif b == 6:
        print("\n離開系統")
        break