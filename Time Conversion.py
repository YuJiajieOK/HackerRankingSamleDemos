#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    h = s[0]+s[1]
    h = int(h)
    Ssize = len(s)
    if s[Ssize-2]=='P'and h!=12:
        h = h+12
        h = h.__str__()
        s = list(s)
        s[0] = h[0]
        s[1] = h[1]
    elif s[Ssize-2]=='A'and h==12:
        s = list(s)
        s[0] = '0'
        s[1] = '0'       
    else:
            s = s
    r = [None]*(Ssize-2)        
    for i in range(Ssize-2):
        s = list(s)
        r[i] = s[i]
    r = ''.join(r)   
    return r     

s = input().strip()
result = timeConversion(s)
print(result)
