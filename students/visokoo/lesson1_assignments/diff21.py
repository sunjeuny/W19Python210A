'''
----------------------------------------------------
Assignment: Python Push Ups - Warmup Part 1 - diff21.py
Author: visokoo | Created: 1/9/2019
ChangeLog: 1/9/2019, Created file 

Given an int n, return the absolute difference between n and 21, 
except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
----------------------------------------------------

'''

def diff21(n):
  if n > 21:
    return abs(21-n)*2
  else:
    return abs(21-n)