#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]

arr_new = set()
for i in range(len(arr)):
    if arr[i] > 5:
        arr_new.add(arr[i] + 2)

print(arr)
print(arr_new)