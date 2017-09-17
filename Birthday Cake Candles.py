
#!/bin/python3
import sys

n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]
hashT = {}
maxHeight = 0
output = 0
for i in range(len(height)):
    hashT[height[i]] = 0
for i in range(len(height)):
    hashT[height[i]] = hashT[height[i]]+1
    if height[i]>maxHeight:
        maxHeight = height[i]
for i in range(len(height)):
    if hashT[height[i]]>output:
        output = hashT[height[i]]
print(output)