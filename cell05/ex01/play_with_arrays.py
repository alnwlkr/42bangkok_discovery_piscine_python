#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]

arr_new = []
for i in range(len(arr)):
    arr_new.append(arr[i] + 2)

print('Original array:',arr)
print('New array:',arr_new)