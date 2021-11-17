# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:01:36 2021

@author: Jay
"""

score = input('英文分數:')
score1 = input('數學分數:')
score = int(score)
score1 = int(score1)
if score > 90 and score1 > 90:
    print('有獎品')
elif score <60 and score1 <60:
    print('要處罰')
