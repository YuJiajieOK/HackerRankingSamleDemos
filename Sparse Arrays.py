import sys

n1 = int(input().strip())
arr1 = [0]*n1
for i in range(n1):
    arr1[i] = [str(input())]

n2 = int(input().strip())
arr2 = [0]*n2
for i in range(n2):
    arr2[i] = [str(input())]

for i in range(len(arr2)):
    Ntem = 0
    for j in range(len(arr1)):
        if arr2[i] == arr1[j]:
            Ntem = Ntem + 1
    print(Ntem)