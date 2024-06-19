#!/usr/bin/env python3

import sys

def end_ism(s):
    s = s.strip()
    if s.endswith('e'):
        s = s[:-1]
    if not s.endswith("ism"):
        return s + "ism"
    return None

argc = len(sys.argv)

if argc == 1:
    print("none")
else:
    argv = sys.argv
    argv.pop(0)
    for s in argv:
        res = end_ism(s)
        if res:
            print(res)