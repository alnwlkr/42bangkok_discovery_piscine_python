#!/usr/bin/env python3

import sys

argc = len(sys.argv)

if argc == 2:
    s = input('What was the parameter? ')
    if s == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")