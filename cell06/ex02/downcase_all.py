#!/usr/bin/env python3

import sys

def downcase_it(s):
    return (s.lower())

argc = len(sys.argv)
argv = sys.argv
argv.pop(0)
if argc >= 2:
    for arg in argv:
        print(downcase_it(arg))
else:
    print("none")