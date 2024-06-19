#!/usr/bin/env python3

import sys

# print(sys.argv)
argc = len(sys.argv)

# print('argc =',argc)
if argc <= 3:
    print("none")
else:
    for i in range(argc - 1, 0, -1):
        print(sys.argv[i])