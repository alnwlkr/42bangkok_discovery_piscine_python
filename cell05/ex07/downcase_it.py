#!/usr/bin/env python3

import sys

# print(sys.argv)
argc = len(sys.argv)

if argc == 1:
    print("none")
else:
    print(sys.argv[1].lower())