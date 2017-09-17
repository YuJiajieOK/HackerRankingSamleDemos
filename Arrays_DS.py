#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
size = len(arr)-1
rarr = [0]*len(arr)
for i in range(len(arr)):
    rarr[i] = arr[size]
    size = size - 1
    print(rarr[i], end=" ")